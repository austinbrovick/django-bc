from django.contrib import admin

from .models import Friendship, FriendshipInvitation

admin.site.register(Friendship)

admin.site.register(FriendshipInvitation)
