from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from project.base.models import BaseModel


class Company(BaseModel):
    type = models.ForeignKey('companies.CompanyType', on_delete=models.PROTECT, verbose_name='Правовая форма',
                             related_name='companies')
    name_short = models.CharField(max_length=255, verbose_name='Сокращенное наименование', unique=True)
    name_full = models.CharField(max_length=255, verbose_name='Полное наименование', unique=True)
    is_customer = models.BooleanField(default=False, verbose_name='Может быть заказчиком')
    is_transporter = models.BooleanField(default=False, verbose_name='Может быть перевозчиком')
    is_own = models.BooleanField(default=False, verbose_name='Своя компания')

    class Meta:
        db_table = 'companies'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return f'{self.type.name_short} {self.name_short}'


class CompanyType(BaseModel):
    name_short = models.CharField(max_length=255, verbose_name='Сокращенное наименование')
    name_full = models.CharField(max_length=255, verbose_name='Полное наименование')

    class Meta:
        db_table = 'company_types'
        verbose_name = 'Организационно-правовая форма'
        verbose_name_plural = 'Организационно-правовые формы'

    def __str__(self):
        return f'{self.name_short} ({self.name_full})'


class Requisites(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Организация',
                                related_name='requisites')
    inn = models.CharField(max_length=20, blank=True, verbose_name='ИНН')
    kpp = models.CharField(max_length=20, blank=True, verbose_name='КПП')
    ogrn = models.CharField(max_length=20, blank=True, verbose_name='ОГРН')
    legal_address = models.CharField(max_length=255, blank=True, verbose_name='Юридический адрес')
    post_address = models.CharField(max_length=255, blank=True, verbose_name='Почтовый адрес')
    fact_address = models.CharField(max_length=255, blank=True, verbose_name='Фактический адрес')
    phone = PhoneNumberField(blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='E-mail')

    class Meta:
        db_table = 'company_requisites'
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'

    def __str__(self):
        return f'Реквизиты {self.company.name_short}'
