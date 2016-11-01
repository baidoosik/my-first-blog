from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^login/$','django.contrib.auth.views.login'),
	url(r'^logout/$',views.logout_page),
	url(r'^password_change/$','django.contrib.auth.views.password_change',
		{'post_change_redirect':'/password_change/done/'}),
	url(r'^password_change/done/$','django.contrib.auth.views.password_change_done'),
	url(r'^register/$',views.register_page)

]