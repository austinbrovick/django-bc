from __future__ import unicode_literals
# from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from profiles.models import UserProfile


class FriendRequestManager(models.Manager):
    def friend_request_status(self, user1, user2):
        frs1 = FriendRequest.objects.filter(from_user=user1).filter(to_user=user2)
        if frs1:
            return 1
        frs2 = FriendRequest.objects.filter(from_user=user2).filter(to_user=user1)
        if frs2:
            return 2
        return 0

    def my_friend_requests(self, me):
        friend_requests = FriendRequest.objects.filter(to_user=me)
        return friend_requests



class FriendRequest(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='user_from')
    to_user = models.ForeignKey(UserProfile, related_name='to_from')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    objects = FriendRequestManager()

    def __unicode__(self):
        return "%s sending a request to %s" %(self.from_user, self.to_user)


class FriendManager(models.Manager):
    def my_friends(self, my_userprofile):
        friends = []
        friends1 = Friend.objects.filter(user_one=my_userprofile)
        friends2 = Friend.objects.filter(user_two=my_userprofile)
        for friend in friends1:
            friends.append(friend.user_two)
        for friend in friends2:
            friends.append(friend.user_one)
        return friends



class Friend(models.Model):
    user_one = models.ForeignKey(UserProfile, related_name='one_user')
    user_two = models.ForeignKey(UserProfile, related_name='two_user')
    friends_since = models.DateTimeField(auto_now_add=True, auto_now=False)
    objects = FriendManager()

    def __unicode__(self):
        return "%s and %s are friends" %(self.user_one, self.user_two)
