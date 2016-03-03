from django.contrib import admin

from .models import FriendRequest, Friendship

admin.site.register(FriendRequest)



class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend_count')
admin.site.register(Friendship, FriendshipAdmin)
