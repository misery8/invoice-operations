from rest_framework import serializers

from src.catalogs.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceStatusReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('status',)
