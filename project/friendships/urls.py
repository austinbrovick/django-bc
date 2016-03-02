from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^my_friends/?', views.my_friends, name='my_friends'),

]

