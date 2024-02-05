from django.db import models
from django.utils.translation import gettext_lazy as _


class Invoice(models.Model):

    class Status(models.TextChoices):
        PENDING_PAYMENT = 'Pending Payment', _('Ожидает оплаты')
        PAID = 'Paid', _('Оплачена')
        CANCELLED = 'Cancelled', _('Отменена')

    status = models.CharField(max_length=20, choices=Status.choices, verbose_name=_('Статус'))
    payment_detail = models.ForeignKey(
        'PaymentDetail',
        on_delete=models.SET_NULL,
        null=True,
        related_name='payment_detail',
        db_index=True
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Сумма')
    )

    class Meta:
        verbose_name = _('Заявка на оплату')
        verbose_name_plural = _('Заявки на оплату')

    def __str__(self):
        return f'{self.status}/{self.payment_detail}/{self.amount}'


class PaymentDetail(models.Model):

    class PaymentType(models.TextChoices):
        CARD = 'Card', _('Карта')
        BANK_ACCOUNT = 'Bank Account', _('Платежный счет')

    class CardType(models.TextChoices):
        MIR = 'MIR', _('Мир')
        VISA = 'VISA', 'Visa'
        MASTERCARD = 'MASTERCARD', 'Mastercard'
        OTHER = 'OTHER', _('Другое')

    payment_type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
        verbose_name=_('Тип платежа')
    )
    card_type = models.CharField(max_length=20, choices=CardType.choices, verbose_name=_('Тип карты/Счета'))
    owner_name = models.CharField(max_length=100, verbose_name=_('ФИО владельца'))
    phone_number = models.CharField(max_length=20, verbose_name=_('Номер телефона'))
    limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Лимит'))

    class Meta:
        verbose_name = _('Реквизит')
        verbose_name_plural = _('Реквизиты')

    def __str__(self):
        return f'{self.owner_name}/{self.card_type}/{self.phone_number}'


