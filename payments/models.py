from django.db import models

from project.base.models import BaseModel


class PaymentForm(BaseModel):
    text = models.CharField('Текст', max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'payment_forms'
        verbose_name = 'Форма оплаты'
        verbose_name_plural = 'Формы оплат'


class PaymentTerm(BaseModel):
    days_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Количество дней')
    DAYS_TYPE_CHOICES = [
        ('bank', 'банковских'),
        ('calendar', 'календарных')
    ]
    days_type = models.CharField(max_length=50, blank=True, choices=DAYS_TYPE_CHOICES, verbose_name='Тип дней')
    condition = models.CharField(max_length=255, verbose_name='Условия')

    def __str__(self):
        days_count = str(self.days_count) + ' ' if self.days_count else ''
        days_type = self.get_days_type_display() + ' дней ' if self.days_type else ''
        return f'{days_count}{days_type}{self.condition}'

    class Meta:
        db_table = 'payment_terms'
        verbose_name = 'Срок оплаты'
        verbose_name_plural = 'Сроки оплат'
