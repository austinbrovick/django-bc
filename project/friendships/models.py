from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_request_from')
    to_user = models.ForeignKey(User, related_name='friend_request_to')
    created_at = models.DateTimeField(default=datetime.datetime.now) # set when the object is created
    accepted = models.BooleanField(default=False) # is the request accepted or is it still pending?

    class Meta:
        unique_together = (('to_user', 'from_user'),)

    def __unicode__(self):
        return "%s sending a request to %s" %(self.from_user, self.to_user)

    def accept(self):
        Friendship.objects.befriend(self.from_user, self.to_user)
        self.accepted = True

    def decline(self):
        self.delete()

    def cancel(self):
        self.delete()

class FriendshipManager(models.Manager):
    def friends_of(self, user): # shuffle = False ??
        queryset = UserProfile.objects.filter(friendship__friends__user=user)
        return queryset

    def hello(self):
        print "hello from model manager"

    def are_friends(self, user1, user2):
        print "are friends"
        friendship = Friendship.objects.get(user=user1)
        return bool(friendship.friends.filter(user=user2).exists())

    def befriend(self, user1, user2):
        print "in befriend function in friendship manager"
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.add(Friendship.objects.get(user=user2))

        FriendshipRequest.objects.filter(from_user=user1, to_user=user2).delete()

    def unfriend(self, user1, user2):
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.remove(Friendship.objects.get(user=user2))

        FriendRequest.objects.filter(from_user=user1, to_user=user2).delete()
        FriendRequest.objects.filter(from_user=user2, to_user=user1).delete()


class Friendship(models.Model):
    user = models.OneToOneField(User, related_name='friendship')
    friends = models.ManyToManyField('self', symmetrical=True) # if i am your friend, you are my friend
    objects = FriendshipManager()

    class Meta:
        verbose_name = 'friendship'
        verbose_name_plural = 'friendships'

    def __unicode__(self):
        return self.user.username

    def friend_count(self):
        return self.friends.count()
















