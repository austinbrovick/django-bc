from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'friend/(?P<username>[\+\w\.@-_]+)/$', views.request_friend, name='request_friend'),


]
