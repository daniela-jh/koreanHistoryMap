from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('khmap.urls')),
    path('api/', include('api.urls')),
    path('search/', include('search_app.urls')),
    url(r'^\.well-known/', include('letsencrypt.urls'))
]