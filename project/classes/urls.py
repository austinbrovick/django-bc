from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^add_classes_page/', views.add_classes_page, name='add_classes_page'),
]
