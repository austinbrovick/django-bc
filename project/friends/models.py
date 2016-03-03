from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, related_name='friend_one')
    from_user = models.ForeignKey(User, related_name='friend_two')
    timestamp = models.DateTimeField(default=timezone.now)

    def accept(self):
        relation1 = Friend.objects.create(from_user=self.from_user, to_user=self.to_user)
        relation2 = Friend.objects.create(from_user=self.to_user, to_user=self.from_user)
        self.delete()





class Friend(models.Model):
    to_user = models.ForeignKey(User, related_name='friends')
    from_user = models.ForeignKey(User, related_name='random_name')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'friend'
        verbose_name_plural = 'friends'
        unique_together = ('from_user', 'to_user')

    def __unicode__(self):
        return self.created_at
