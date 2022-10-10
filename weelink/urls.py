
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('adminlar/', admin.site.urls),
    path('', include('base.urls')),
    path('accounts/', include('allauth.urls')),
    #api only
    path('api/', include('api.urls')),
]
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]