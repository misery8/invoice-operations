from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from .models import Invoice, PaymentDetail


class BaseListView(ListView):

    paginate_by = 50

    def get(self, request, *args, **kwargs):
        self.paginate_by = request.GET.get('limit', self.paginate_by)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.request.GET:
            filter_params = {k: v for k, v in self.request.GET.items() if k != 'column' or k != 'direction'}
            context['filter_params'] = urlencode(filter_params)
        return context


class InvoiceListView(BaseListView):

    extra_context = {
        'title': Invoice._meta.verbose_name_plural
    }
    model = Invoice
    template_name = 'catalogs/invoice_list.html'
    ordering = ['-id']


class PaymentDetailListView(LoginRequiredMixin, BaseListView):

    extra_context = {
        'title': PaymentDetail._meta.verbose_name_plural,
    }
    model = PaymentDetail
    template_name = 'catalogs/payment_detail_list.html'
    ordering = ['-id']

    def get_queryset(self):
        if self.request.GET.get('column') and self.request.GET.get('direction'):
            direction = '-' if self.request.GET['direction'] == 'desc' else ''
            self.ordering = [f'{direction}{self.request.GET["column"]}']

        if self.request.GET.get('q'):
            search = self.request.GET['q']
            if search.strip():
                value = search.strip()
                filter_params = Q(
                    Q(id__icontains=value) | Q(payment_type__icontains=value) |
                    Q(card_type__icontains=value) | Q(owner_name__icontains=value) |
                    Q(phone_number__icontains=value) | Q(limit__icontains=value)
                )
                self.queryset = PaymentDetail.objects.filter(filter_params)
        return super().get_queryset()
