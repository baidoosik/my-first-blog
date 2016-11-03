from django.conf.urls import url
from django.contrib.auth.views import login 
from . import views
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.conf.urls import include


urlpatterns = [
	url(r'^$',views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$',views.logout_page, name='logout_page'),
	url(r'^password_change/$',password_change, name='password_change'),
	url(r'^password_change/done/$',password_change_done, name='password_change_done'),
	url(r'^register/$',views.register_page, name='register'),
	url(r'^user/(\w+)/$', views.user_page),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]