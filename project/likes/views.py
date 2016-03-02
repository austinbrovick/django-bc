# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from .models import PostLike, CommentLike
# from django.apps import apps
# Post = apps.get_app_config('posts').models['post']
# Comment = apps.get_app_config('posts').models['comment']

# @login_required
# def like_post(request, post_id):
#     if request.method == 'POST':
#         instance = PostLike()
#         instance.post = Post.objects.get(id=post_id)
#         instance.liker = request.user.userprofile
#         instance.save()
#         return redirect('my_profile')
#     else:
#         return HttpResponse("you suck balls")


# @login_required
# def like_comment(request, comment_id):
#     print "in like comment function "
#     if request.method == 'POST':
#         instance = CommentLike()
#         instance.comment = Comment.objects.get(id=comment_id)
#         instance.liker = request.user.userprofile
#         instance.save()
#         return redirect('my_profile')
#     else:
#         return HttpResponse("comment like")
