from django.db import models
from profiles.models import UserProfile



def upload_location_post(instance, filename):
    user = str(instance.user.user.id)
    post = str(instance.id)
    return "%s/posts/%s" %(user, filename)

def upload_location_comment(instance, filename):
    post_user = str(instance.post.user.user.id)
    comment_user = str(instance.user.user.id)
    post = str(instance.post.id)
    return "%s/%s/%s/%s" %(post_user, post, comment_user, filename)

class PostManager(models.Manager):
    def my_profile_posts(self, me):
        my_profile_posts = Post.objects.filter(profile=me)
        return my_profile_posts


    def their_profile_posts(self, me, them):
        their_profile_posts = Post.objects.filter(profile=them)
        posts = []
        count = -1
        for post in their_profile_posts:
            count = count + 1
            posts.append({'post':post, 'likes':Post.objects.filter(postlike__post=post).count(), 'likers' :UserProfile.objects.filter(postlike__post=post), 'comments': Comment.objects.filter(post=post), 'like_status' : False})
            for liker in posts[count]["likers"]:
                if liker == me:
                    posts[count]['like_status'] = True
        return posts



class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='poster')
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    post_picture = models.ImageField(upload_to=upload_location_post, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, related_name='profile', default=None, blank=True, null=True)
    objects = PostManager()

    def __unicode__(self):
        return self.text


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment_picture = models.ImageField(upload_to=upload_location_comment, null=True, blank=True)

    def __unicode__(self):
        return self.text



class PostLike(models.Model):
    post = models.ForeignKey(Post)
    liker = models.ForeignKey(UserProfile)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.post.text

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    liker = models.ForeignKey(UserProfile)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.comment.text
