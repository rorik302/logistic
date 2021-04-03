from django.db import models

from companies.models import Company
from project.base.models import BaseModel, Phone


class Driver(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', related_name='drivers')
    full_name = models.CharField('ФИО', max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'drivers'
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class DriverPhone(Phone):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Водитель', related_name='phones')

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'drivers_phones'
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны водителей'


class DriverLicense(BaseModel):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Водитель', related_name='licenses')
    serial = models.CharField('Серийный номер', max_length=10)
    number = models.CharField('Номер', max_length=20)
    start_date = models.DateField('Дата выдачи')
    expiration_date = models.DateField('Дата окончания')

    def __str__(self):
        return f'Вод. удост. {self.driver.full_name}'

    class Meta:
        db_table = 'drivers_licenses'
        verbose_name = 'Водительское удостоверение'
        verbose_name_plural = 'Водительские удостоверения'


class DriverPassport(BaseModel):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Водитель', related_name='passports')
    serial = models.CharField('Серийный номер', max_length=10)
    number = models.CharField('Номер', max_length=20)
    issued_by = models.CharField('Кем выдан', max_length=255)
    issue_date = models.DateField('Дата выдачи')

    def __str__(self):
        return f'Паспорт {self.driver.full_name}'

    class Meta:
        db_table = 'drivers_passports'
        verbose_name = 'Паспорт водителя'
        verbose_name_plural = 'Паспорта водителей'
