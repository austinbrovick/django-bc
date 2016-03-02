from __future__ import unicode_literals

from django.db import models
from profiles.models import UserProfile




# class FriendshipManager(models.Manager):
#     def my_friends(self, user):
#         friends1 = UserProfile.objects.filter(requester=user).filter(friends=True)
#         friends2 = UserProfile.objects.filter(receiver=user).filter(friends=True)
#         friends = []
#         for friend in friends1:
#             friends.append(friend)
#         for friend in friends2:
#             friends.append(friend)
#         return friends



class Friendship(models.Model):
    requester = models.ForeignKey(UserProfile, related_name='requester')
    receiver = models.ForeignKey(UserProfile, related_name='receiver')
    sent_status = models.BooleanField(default=False)
    accepted_status = models.BooleanField(default=False)
    friends = models.BooleanField(default=False)
    time_sent = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_accepted = models.DateTimeField(auto_now_add=True, auto_now=False)
    friend = models.ForeignKey(UserProfile, related_name='friend')


    def __unicode__(self):
        return self.requester.user.first_name

    # def my_friends(self, user):
    #     friends1 = UserProfile.objects.filter(requester=user.userprofile).filter(friends=True)
    #     friends2 = UserProfile.objects.filter(receiver=user.userprofile).filter(friends=True)
    #     friends = []
    #     for friend in friends1:
    #         friends.append(friend)
    #     for friend in friends2:
    #         friends.append(friend)
    #     return friends




# request.user.userprofile.requester
