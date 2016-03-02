from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.apps import apps


from posts.forms import PostForm, CommentForm

Post = apps.get_app_config('posts').models['post']
Comment = apps.get_app_config('posts').models['comment']
PostLike = apps.get_app_config('posts').models['postlike']
CommentLike = apps.get_app_config('posts').models['commentlike']
Friendship = apps.get_app_config('friendships').models['friendship']
# PostForm = apps.get_app_config('posts').forms['postform']

from posts.forms import PostForm, CommentForm
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def my_profile(request):
    my_profile, created = UserProfile.objects.get_or_create(user=request.user)
    my_posts = Post.objects.filter(user=request.user.userprofile).order_by('-created_at')
    comments = Comment.objects.all()
    all_users = UserProfile.objects.all().exclude(user=request.user)
    post_form = PostForm()
    comment_form = CommentForm()
    post_list = []
    count = -1
    for post in my_posts:
        count = count + 1
        post_list.append({'post':post, 'likes': Post.objects.filter(postlike__post=post).count(), 'likers': UserProfile.objects.filter(postlike__post=post), 'comments' : Comment.objects.filter(post=post), 'like_status' : False})
        for liker in post_list[count]["likers"]:
            if liker == request.user.userprofile:
                post_list[count]['like_status'] = True
                break

    print post_list

    context = {
        "my_profile" : my_profile,
        "post_form" : post_form,
        "comment_form" : comment_form,
        "comments" : comments,
        "post_list" : post_list,
        "current_user" : request.user.userprofile,
        "all_users" : all_users,
    }
    print post_list
    return render(request, "profiles/my_profile.html", context)

@login_required
def their_profile(request, username):
    their_profile = UserProfile.objects.get(user__username=username)
    context = {
        "their_profile" : their_profile,
    }
    return render(request, "profiles/their_profile.html", context)
    return HttpResponse("their profile")

@login_required
def edit_profile_page(request):
    my_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_form = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=user_form)
    context = {
       "my_profile" : my_profile,
       "form" : form,
    }
    return render(request, "profiles/edit_profile.html", context)


@login_required
def edit_profile(request):
    print "in edit profile"
    my_profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=my_profile)
    print form
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("my_profile")
    else:
        return redirect("edit_profile_page")
