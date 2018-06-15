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
from . import view_api as views

urlpatterns = [
    url(r'^detail/(?P<id>[0-9]+)/$', views.FruitDetail.as_view(), name='detail'),
    url(r'^list/$', views.FruitList.as_view(), name='fruit_list'),
    url(r'^tags/$', views.tag_list, name='tag_list'),
    url(r'^activity/list/$', views.ActivityList.as_view(), name='activity_list'),
    url(r'^activity/detail/(?P<id>[0-9]+)/$', views.ActivityDetail.as_view(), name='activity_detail'),
]
