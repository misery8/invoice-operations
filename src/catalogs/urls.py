from django.urls import path
from .views import (
    InvoiceListView,
    PaymentDetailListView,
)

urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoice_list'),
    path('payment-details/', PaymentDetailListView.as_view(), name='payment_detail_list'),
]
