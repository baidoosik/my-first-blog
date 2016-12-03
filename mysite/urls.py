from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^accounts/login/$', django.contrib.auth.views.login),
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
