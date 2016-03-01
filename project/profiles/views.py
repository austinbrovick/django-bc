from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.apps import apps


from posts.forms import PostForm, CommentForm

Post = apps.get_app_config('posts').models['post']
Comment = apps.get_app_config('posts').models['comment']
# PostForm = apps.get_app_config('posts').forms['postform']


from posts.forms import PostForm, CommentForm
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def my_profile(request):
    my_profile, created = UserProfile.objects.get_or_create(user=request.user)
    my_posts = Post.objects.filter(user=request.user.userprofile).order_by('-created_at')
    comments = Comment.objects.all()
    post_form = PostForm()
    comment_form = CommentForm()
    context = {
        "my_profile" : my_profile,
        "post_form" : post_form,
        "comment_form" : comment_form,
        "my_posts" : my_posts,
        "comments" : comments,
    }

    return render(request, "profiles/my_profile.html", context)

@login_required
def their_profile(request, username):
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
