from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, PostLike, CommentLike
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PostForm, CommentForm


@login_required
def post(request):
    print "made it to post"
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print "form is valid 1"
            instance = form.save(commit=False)
            print "form is valid 2"
            instance.user = request.user.userprofile
            print "form is valid 3"
            instance.save()
            return redirect('my_profile')
        else:
            return redirect('my_profile')
    # return redirect("my_profile")

@login_required
def comment(request, post_id):
    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = Post.objects.get(id=post_id)
        instance = form.save(commit=False)
        instance.user = request.user.userprofile
        instance.post = post
        instance.save()
        return redirect('my_profile')
    else:
        return redirect('my_profile')


@login_required
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('my_profile')
    else:
        return HttpResponse("you can't do that!!")

@login_required
def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect('my_profile')
    else:
        return HttpResponse("you can't do that!!")


@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    instance = PostLike()
    instance.post = post
    instance.liker = request.user.userprofile
    instance.save()
    return redirect('my_profile')





@login_required
def unlike_post(request, post_id):
    post = Post.objects.get(id=post_id)
    instance = PostLike.objects.get(post=post)
    instance.delete()
    return redirect('my_profile')






