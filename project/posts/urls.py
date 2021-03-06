from django.conf.urls import url
from . import views

print "made it to posts urls"

urlpatterns = [
    url(r'^post/$', views.post, name='post'),
    url(r'^comment/(?P<post_id>\d+)', views.comment, name='comment'),
    url(r'^post/delete/(?P<post_id>\d+)', views.delete_post, name='delete_post'),
    url(r'^comment/delete/(?P<comment_id>\d+)', views.delete_comment, name='delete_comment'),
    url(r'^post/like/(?P<post_id>\d+)', views.like_post, name='like_post'),
    url(r'^post/unlike/(?P<post_id>\d+)', views.unlike_post, name='unlike_post'),
    url(r'^post_on_their_profile/(?P<username>[\+\w\.@-_]+)/$', views.post_on_their_profile, name='post_on_their_profile'),
    url(r'^delete_post_on_their_profile/(?P<post_id>\d+)/(?P<username>[\+\w\.@-_]+)/$', views.delete_post_on_their_profile, name='delete_post_on_their_profile')
]
