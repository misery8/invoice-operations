from django import forms

from .models import Invoice, PaymentDetail


class InvoiceForm(forms.ModelForm):

    payment_detail = forms.CharField(
        label='Реквизиты',
        widget=forms.ModelChoiceField(
            queryset=PaymentDetail.objects.all(),
            attrs={'class': 'form-control transaction'}
        )
    )

    amount = forms.DecimalField(
        label='Сумма',
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control transaction',
                'placeholder': '...'
            }
        )
    )

    status = forms.CharField(
        label='Статус',
        widget=forms.ChoiceField(
            attrs={'class': 'form-control transaction'}
        )
    )

    class Meta:
        model = Invoice
        fields = ('status', 'payment_detail', 'amount')


class PaymentDetailForm(forms.ModelForm):

    payment_type = forms.CharField(
        label='Тип платеж',
        widget=forms.ChoiceField(
            attrs={'class': 'form-control'}
        )
    )

    card_type = forms.CharField(
        label='Тип карты/Счета',
        widget=forms.ChoiceField(
            attrs={'class': 'form-control'}
        )
    )

    owner_name = forms.CharField(
        label='ФИО Владельца',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    limit = forms.CharField(
        label='Лимит',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = PaymentDetail
        fields = ('payment_type', 'card_type', 'owner_name', 'phone_number', 'limit')
