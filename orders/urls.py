from django.conf.urls import url
from . import views_api as views

urlpatterns = [
	url(r'^create/$', views.OrderList.as_view(), name='order_create'),
        url(r'^list/$', views.OrderList.as_view(), name='order_list'),
        url(r'^change_status/(?P<id>\d+)/$', views.OrderList.as_view(), name='change_status'),
        url(r'^detail/(?P<pk>\d+)/$', views.OrderDetail.as_view(), name='order_detail')
]
