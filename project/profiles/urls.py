
from django.conf.urls import url
from . import views

print "made it to project urls"

urlpatterns = [
    url(r'^$', views.my_profile, name='my_profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^edit/', views.edit_profile_page, name='edit_profile_page'),
    url(r'^(?P<username>[\w.@+-]+)/', views.their_profile, name='their_profile'),
]
