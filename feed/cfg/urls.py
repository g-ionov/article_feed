from django.contrib import admin
from django.urls import path, include
from cfg import settings
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('feed_app.urls')),
    path('api-register/', include('register.urls')),


]

urlpatterns += yasg_urls

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
