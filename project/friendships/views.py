from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Friendship


@login_required
def my_friends(request):
    if request.method == 'POST':
        friends1 = Friendship.objects.filter(requester=request.user.userprofile).filter(friends=True)
        friends2 = Friendship.objects.filter(receiver=request.user.userprofile).filter(friends=True)
        friends = []
        for friend in friends1:
            friends.append(friend)
        for friend in friends2:
            friends.append(friend)
        context = {
            "my_friends" : friends,
            "me" : request.user.userprofile,
        }
        print friends
        return render(request, 'friendships/friends.html', context)

