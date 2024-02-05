import random

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from transliterate import translit

from src.catalogs.models import Invoice, PaymentDetail


class Command(BaseCommand):

    help = 'Наполняет таблицы данными'
    fake = Faker('ru_RU')

    @transaction.atomic
    def handle(self, *args, **options):

        try:
            payment_details = self.create_payment_details()
            self.create_invoice(payment_details)
            self.stdout.write(
                self.style.SUCCESS('Successfully created')
            )
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'Something went wrong: {e}')
            )

    def create_payment_details(self):

        pyment_details = []
        payment_types = list(PaymentDetail.PaymentType)
        card_types = list(PaymentDetail.CardType)
        for i in range(100):
            pyment_details.append(PaymentDetail(
                payment_type=random.choice(payment_types),
                card_type=random.choice(card_types),
                phone_number=self.fake.phone_number(),
                owner_name=translit(self.fake.name(), language_code='ru', reversed=True),
                limit=self.fake.pydecimal(right_digits=2, positive=True, min_value=1, max_value=999)
            ))

        return PaymentDetail.objects.bulk_create(pyment_details)

    def create_invoice(self, payment_details):

        invoices = []
        statuses = list(Invoice.Status)
        for i in range(5000):
            invoices.append(Invoice(
                status=random.choice(statuses),
                payment_detail=random.choice(payment_details),
                amount=self.fake.pydecimal(right_digits=2, positive=True, min_value=1, max_value=999)
            ))
        return Invoice.objects.bulk_create(invoices)
