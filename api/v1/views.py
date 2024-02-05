from rest_framework import generics

from src.catalogs.models import Invoice
from .serializers import InvoiceSerializer, InvoiceStatusReadSerializer


class InvoiceCreateAPIView(generics.CreateAPIView):

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceStatusReadAPIView(generics.RetrieveAPIView):

    queryset = Invoice.objects.all()
    serializer_class = InvoiceStatusReadSerializer
