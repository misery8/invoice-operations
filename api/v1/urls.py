from django.urls import path

from .views import InvoiceCreateAPIView, InvoiceStatusReadAPIView

urlpatterns = [
    path('invoices/', InvoiceCreateAPIView.as_view()),
    path('invoices/<int:pk>/status/', InvoiceStatusReadAPIView.as_view()),
]
