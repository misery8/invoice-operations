from django.urls import path

from .views import UserUpdateView

urlpatterns = [
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit')
]
