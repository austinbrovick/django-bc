from django.shortcuts import render
from django.http import HttpResponseBadRequest, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FriendRequest, Friendship
from django.views.generic import View
from django.contrib.auth.models import User


@login_required
def friend_request_request(request, username):
    user = User.objects.get(username=username)
    instance = FriendRequest()
    instance.from_user = request.user
    instance.to_user = user
    instance.save()



    # Friendship.objects.hello()
    # Friendship.objects.are_friends()


    # Friendship.objects.befriend(user, request.user)

    # print Friendship.objects.are_friends(user, user)
    # if Friendship.objects.are_friends(request.user, user):
    #     return HttpResponse("You are already friends")
    # try:
    #     friend_request = FriendRequest.objects.get(from_user=user, to_user=request.user)
    #     if friend_request:
    #         friend_request.accept()
    # except Http404:
    #     FriendRequest.objects.create(
    #             from_user=request.user,
    #             to_user=user
    #         )
    #     return HttpResponse("holla holla")
    return HttpResponse("in friend request method")





