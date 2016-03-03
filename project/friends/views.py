from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import FriendRequest, Friend


def request_friend(request, username):
    receiver = User.objects.get(username=username)
    FriendRequest.objects.create(to_user=receiver, from_user=request.user)
    return HttpResponse("yay")
