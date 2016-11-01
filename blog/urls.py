from django.conf.urls import url
from django.contrib.auth.views import login 
from . import views
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done


urlpatterns = [
	url(r'^$',views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$',views.logout_page, name='logout_page'),
	url(r'^password_change/$',password_change, name='password_change'),
	url(r'^password_change/done/$',password_change_done, name='password_change_done'),
	url(r'^register/$',views.register_page)

]