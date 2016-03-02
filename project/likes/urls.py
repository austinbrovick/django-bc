from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<post_id>\d+)', views.like_post, name='like_post'),
    url(r'^comment/(?P<comment_id>\d+)', views.like_comment, name='like_comment'),
]
