from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ContentView

content_list = ContentView.as_view({
    'post': 'create',
    'get': 'list',
})

content_detail = ContentView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contents/', content_list, name='content_list'),
    path('contents/<int:pk>/', content_detail, name='content_detail')
])