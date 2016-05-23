from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^oficina/$',views.oficina),
	url(r'^producto/$',views.producto),
	url(r'^contactos/$',views.contactos),
	url(r'^login/$',views.login),
	url(r'^registro/$',views.registro),
	url(r'^institucional/$',views.institucional),
	url(r'^exportacion/$',views.exportacion),
]