from django.conf.urls import url
from . import views

print "made it to posts urls"

urlpatterns = [
    url(r'^post/', views.post, name='post'),
    url(r'^comment/(?P<post_id>\d+)', views.comment, name='comment'),


]
