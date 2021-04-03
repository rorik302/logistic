from django.db import models

from project.base.models import BaseModel


class Vehicle(BaseModel):
    TYPE_CHOICES = [
        ('auto', 'Авто'),
        ('trailer', 'Прицеп')
    ]
    type = models.CharField(max_length=50, verbose_name='Тип ТС', choices=TYPE_CHOICES)
    mark = models.CharField(max_length=255, verbose_name='Марка', blank=True)
    registration_number = models.CharField(max_length=25, verbose_name='Регистрационный номер')

    def __str__(self):
        return f'{self.mark} {self.registration_number}'.strip()

    class Meta:
        db_table = 'vehicles'
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'


class VehicleParameters(BaseModel):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Транспортное средство')
    body = models.CharField(max_length=50, verbose_name='Кузов', blank=True)
    carrying = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Грузоподъемность')
    volume = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Объем')
    length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Длина')
    width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ширина')
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Высота')
    top = models.BooleanField(default=False, verbose_name='Верхняя загрузка/выгрузка')
    side = models.BooleanField(default=False, verbose_name='Боковая загрузка/выгрузка')
    back = models.BooleanField(default=True, verbose_name='Задняя загрузка/выгрузка')
    tail_lift = models.BooleanField(default=False, verbose_name='Гидроборт')

    def __str__(self):
        return f'Параметры ТС {self.vehicle.mark + " " if self.vehicle.mark else ""}{self.vehicle.registration_number}'

    class Meta:
        db_table = 'vehicle_parameters'
        verbose_name = 'Параметры транспортного средства'
        verbose_name_plural = 'Параметры транспортных средств'
