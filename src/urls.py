from django.urls import include, path

from .views import index

urlpatterns = [
    path('auth/', include('src.auth.urls')),
    path('catalogs/', include('src.catalogs.urls')),
    path('users/', include('src.users.urls')),
    path('', index, name='index'),
]
