from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^add_classes_page/', views.add_classes_page, name='add_classes_page'),
    url(r'^add_classes/(?P<quarter>[a-zA-Z\d]+)/$', views.add_classes, name='add_classes'),
    url(r'^quarter/(?P<quarter>[a-zA-Z\d]+)/$', views.quarter, name='quarter')
]


                # {{ formset.management_form }}
                # <ul>
                #     {% for form in formset %}
                #         <li>{{ form }}</li>
                #         <br/>
                #     {% endfor %}
                # </ul>
