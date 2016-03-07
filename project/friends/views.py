from django.shortcuts import render, redirect
from django.apps import apps
from django.http import HttpResponse
from .models import FriendRequest, Friend
UserProfile = apps.get_app_config('profiles').models['userprofile']


def request_friend(request, username):
    from_user = UserProfile.objects.get(user__username=request.user.username)
    print "from user: ", from_user
    to_user = UserProfile.objects.get(user__username=username)
    print "to user:   ", to_user


    fr = FriendRequest()
    fr.from_user = from_user
    fr.to_user = to_user
    fr.save()
    return HttpResponse("yay")



def notifications(request):
    me = UserProfile.objects.get(user__username=request.user.username)
    my_friend_requests = FriendRequest.objects.my_friend_requests(me)
    print my_friend_requests
    context = {
        "friend_requests" : my_friend_requests,
    }
    return render(request, "nots/nots.html", context)


def accept_request(request, username):
    friend_request_from = UserProfile.objects.get(user__username=username)
    friends = Friend()
    friends.user_one = friend_request_from
    friends.user_two = request.user.userprofile
    friends.save()

    friend_request = FriendRequest.objects.filter(from_user=friend_request_from).filter(to_user=request.user.userprofile)
    friend_request.delete()

    return redirect('notifications')

