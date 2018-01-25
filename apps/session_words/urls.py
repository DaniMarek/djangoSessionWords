from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^addsesh$', views.addsesh),
	url(r'^clearsesh$', views.clearsesh),
]