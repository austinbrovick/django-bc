
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'request/(?P<username>[\+\w\.@-_]+)/$', views.friend_request_request, name='friend_request_request'),

]
