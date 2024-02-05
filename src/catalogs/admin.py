from django.contrib import admin

from .models import Invoice, PaymentDetail


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    list_display = ('id', 'status', 'payment_detail', 'amount')
    search_fields = ['id']


@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):

    list_display = ('id', 'payment_type', 'card_type', 'owner_name', 'phone_number')
    search_fields = ['id']
