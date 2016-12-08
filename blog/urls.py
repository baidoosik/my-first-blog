from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.conf.urls import include


urlpatterns = [
	url(r'^$',views.first_page,name='first_view'),
	url(r'^thankq/list$',views.thankq_list_page,name='thankq_list'),
	url(r'^cow/list$',views.cow_list_page,name='cow_list'),
	url(r'^thankq/starbucks/list$',views.starbucks_list_page,name='starbucks_list'),
	url(r'^thankq/coffeebean/list$',views.coffeebean_list_page,name='coffeebean_list'),
	url(r'^man/new$',views.man_new,name='man_new'),
	url(r'^woman/new$',views.woman_new,name='woman_new'),
	url(r'^cow/finish$',views.cow_finish,name='cow_finish'),
	url(r'^post/list$',views.post_list, name = 'post_list'),
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
