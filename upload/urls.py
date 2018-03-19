from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^uploader/upload_form/$', views.upload_form, name="upload_form"),
    url(r'^uploader/upload/$', views.upload, name="upload"),
    url(r'^uploader/upload_progress/$', views.upload_progress, name="upload_progress"),
    url(r'^uploader/finish_upload/$', views.finish_upload, name="finish_upload"),
]
