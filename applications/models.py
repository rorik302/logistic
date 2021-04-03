from django.db import models

from companies.models import Company
from drivers.models import Driver
from payments.models import PaymentForm, PaymentTerm
from project.base.models import BaseModel
from vehicles.models import Vehicle


class Application(BaseModel):
    outgoing_number = models.CharField(max_length=50, verbose_name='Исходящий номер', unique=True)
    outgoing_date = models.DateField(verbose_name='Исходящая дата')
    incoming_number = models.CharField(max_length=50, blank=True, verbose_name='Входящий номер')
    incoming_date = models.DateField(null=True, blank=True, verbose_name='Входящая дата')
    own_company_with_customer = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='own_company_with_customer_applications',
        verbose_name='Своя компания с заказчиком',
        limit_choices_to={'is_own': True})
    own_company_with_transporter = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='own_company_with_transporter_applications',
        verbose_name='Своя компания с перевозчиком',
        limit_choices_to={'is_own': True})
    customer = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='customer_applications',
        verbose_name='Заказчик',
        limit_choices_to={'is_customer': True})
    transporter = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='transporter_applications',
        verbose_name='Перевозчик',
        limit_choices_to={'is_transporter': True})
    vehicles = models.ManyToManyField(Vehicle, verbose_name='Транспортные средства', related_name='applications')
    drivers = models.ManyToManyField(Driver, verbose_name='Водители', related_name='applications')
    customer_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ставка заказчика')
    transporter_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ставка перевозчику')
    customer_payment_form = models.ForeignKey(
        PaymentForm,
        on_delete=models.PROTECT,
        related_name='customer_payment_form',
        verbose_name='Форма оплаты с заказчиком')
    transporter_payment_form = models.ForeignKey(
        PaymentForm,
        on_delete=models.PROTECT,
        related_name='transporter_payment_form',
        verbose_name='Форма оплаты с перевозчиком')
    customer_payment_term = models.ForeignKey(
        PaymentTerm,
        on_delete=models.PROTECT,
        related_name='customer_payment_term',
        verbose_name='Срок оплаты с заказчиком')
    transporter_payment_term = models.ForeignKey(
        PaymentTerm,
        on_delete=models.PROTECT,
        related_name='transporter_payment_term',
        verbose_name='Срок оплаты с перевозчиком')
    customer_penalties = models.TextField(verbose_name='Штрафные санкции с заказчиком', blank=True)
    transporter_penalties = models.TextField(verbose_name='Штрафные санкции с перевозчиком', blank=True)
    customer_additional_conditions = models.TextField(verbose_name='Дополнительные условия с заказчиком', blank=True)
    transporter_additional_conditions = models.TextField(verbose_name='Дополнительные условия с перевозчиком',
                                                         blank=True)

    def __str__(self):
        return f'Заявка №{self.outgoing_number} от {self.outgoing_date}'

    class Meta:
        db_table = 'applications'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
