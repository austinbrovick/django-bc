from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'friend/(?P<username>[\+\w\.@-_]+)/$', views.request_friend, name='request_friend'),
    url(r'notifications/', views.notifications, name='notifications'),
    url(r'accept_request/(?P<username>[\+\w\.@-_]+)/$', views.accept_request, name='accept_request')
]
