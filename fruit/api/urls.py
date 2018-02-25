from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^fruit/$',
			views.FruitListView.as_view(),
			name='fruit_list'),
		url(r'^fruit/(?P<pk>\d+)/$',
			views.FruitDetailView.as_view(),
			name='fruit_detail'),
]