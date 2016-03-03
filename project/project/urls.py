"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/accounts/login'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^classes/', include('classes.urls')),
    url(r'^post/', include('posts.urls')),
    url(r'^friends/', include('friends.urls')),
    # url(r'^like/', include('likes.urls')),
    url(r'^', include('home_page.urls')),

]

if settings.DEBUG: # == True
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






# (?P<username>[\w.@+-]+)
# url(?P<username>[\w.@+-]+)$', 'appname.views.show_user'),
# (?P<order>\d+)
# (?P<username>[\w.@+-]+)/(?P<order>\d+)
