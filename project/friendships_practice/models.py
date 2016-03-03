from __future__ import unicode_literals
import datetime
from django.db import models
from django.core.urlresolvers import reverse

from profiles.models import UserProfile


class FriendshipManager(models.Manager):
    def friends_for_user(self, user):
        friends = []
        for friendship in self.filter(from_user=user).select_related(depth=1):
            friends.append({"friend" : friendship.to_user, "friendship": friendship})
        for friendship in self.filter(to_user=user).select_related(depth=1):
            friends.append({"friend" : friendship.from_user, "friendship" : friendship})
        return friends

    def are_friends(self, user1, user2):
        if self.filter(from_user=user1, to_user=user2).count() > 0:
            return true
        if self.filter(from_user=user2, to_user=user1).count() > 0:
            return true
        return false

    def unfriend(self, user1, user2):
        if self.filter(from_user=user1, to_user=user2):
            friendship = self.filter(from_user=user1, to_user=user2)
        elif self.filter(from_user=user2, to_user=user1):
            friendship = self.filter(from_user=user2, to_user=user1)
        friendship.delete()

class Friendship(models.Model):
    to_user = models.ForeignKey(UserProfile, related_name='receiver')
    from_user = models.ForeignKey(UserProfile, related_name='requester')
    became_friends = models.DateField(default=datetime.date.today)
    objects = FriendshipManager()

    class Meta:
        unique_together = (('to_user', 'from_user'),)

def friend_set_for(user):
    return set([obj['friend'] for obj in Friendship.objects.friends_for_user(user)])


FRIEND_STATUS = (
    ('Sent', 'Sent'),
    ('Failed', 'Failed'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined'),
    ('Deleted', 'Deleted'),
)



# class FriendshipInvitationManager(models.Manager):
#     def invitations(self, *args, **kwargs):
#         return self.filter(*args, **kwargs).exclude(status__in=["6", "8"])


class FriendshipInvitation(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='invite_from')
    to_user = models.ForeignKey(UserProfile, related_name='invite_to')
    sent = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=20, choices=FRIEND_STATUS)

    # objects = FriendshipInvitationManager() ???

    def accept(self):
        if not Friendship.objects.are_friends(self.to_user, self.from_user):
            friendship = Friendship(to_user=self.to_user, from_user=self.from_user)
            friendship.save()
    def decline(self):
        if not Friendship.objects.are_friends(self.to_user, self.from_user):
            self.status = 'Declined'
            self.save()


























