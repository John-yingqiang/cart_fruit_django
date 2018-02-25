"""Thai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from . import views
from . import APIviews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/fruits/$', APIviews.FruitListAPI.as_view(), name='fruits_list'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^video/$', views.get_video, name='video'),
    url(r'^more/(?P<tags>[\w]+)/$', views.more, name='more'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^activity/(?P<id>\d+)/$', views.relative_activity, name='activity'),
]