# from __future__ import unicode_literals
# from profiles.models import UserProfile
# from posts.models import Post, Comment
# from django.db import models







# class PostLike(models.Model):
#     post = models.ForeignKey(Post)
#     liker = models.ForeignKey(UserProfile)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

#     def __unicode__(self):
#         return self.post.text


# class CommentLike(models.Model):
#     comment = models.ForeignKey(Comment)
#     liker = models.ForeignKey(UserProfile)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

#     def __unicode__(self):
#         return self.comment.text
