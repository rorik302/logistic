from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from uuslug import uuslug

from project.base.models import BaseModel


class Company(BaseModel):
    type = models.ForeignKey('companies.CompanyType', on_delete=models.PROTECT, verbose_name='Правовая форма',
                             related_name='companies')
    name_short = models.CharField(max_length=255, verbose_name='Сокращенное наименование')
    name_full = models.CharField(max_length=255, verbose_name='Полное наименование')
    is_customer = models.BooleanField(default=False, verbose_name='Может быть заказчиком')
    is_transporter = models.BooleanField(default=False, verbose_name='Может быть перевозчиком')
    is_own = models.BooleanField(default=False, verbose_name='Своя компания')
    slug = models.CharField('Слаг', max_length=50, blank=True)

    class Meta:
        db_table = 'companies'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return f'{self.type.name_short} {self.name_short}'

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name_short, instance=self)
        super(Company, self).save(*args, **kwargs)


class CompanyType(BaseModel):
    name_short = models.CharField(max_length=255, verbose_name='Сокращенное наименование')
    name_full = models.CharField(max_length=255, verbose_name='Полное наименование')
    slug = models.CharField('Слаг', max_length=50, blank=True)

    class Meta:
        db_table = 'company_types'
        verbose_name = 'Организационно-правовая форма'
        verbose_name_plural = 'Организационно-правовые формы'

    def __str__(self):
        return f'{self.name_short} ({self.name_full})'

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name_short, instance=self)
        super(CompanyType, self).save(*args, **kwargs)


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
    slug = models.CharField('Слаг', max_length=50, blank=True)

    class Meta:
        db_table = 'company_requisites'
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'

    def __str__(self):
        return f'Реквизиты {self.company.name_short}'

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.company.name_short, instance=self)
        super(Requisites, self).save(*args, **kwargs)
