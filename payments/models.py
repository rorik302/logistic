from django.db import models

from project.base.models import BaseModel


class PaymentForm(BaseModel):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        db_table = 'payment_forms'
        verbose_name = 'Форма оплаты'
        verbose_name_plural = 'Формы оплат'


class PaymentTerm(BaseModel):
    days_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Количество дней')
    DAYS_TYPE_CHOICES = [
        ('bank', 'банковские'),
        ('calendar', 'календарные')
    ]
    days_type = models.CharField(max_length=50, blank=True, choices=DAYS_TYPE_CHOICES, verbose_name='Тип дней')
    condition = models.CharField(max_length=255, verbose_name='Условия')

    def __str__(self):
        return f'{self.days_count} {self.days_type} {self.condition}'

    class Meta:
        db_table = 'payment_terms'
        verbose_name = 'Срок оплаты'
        verbose_name_plural = 'Сроки оплат'
