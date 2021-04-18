from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Phone(models.Model):
    TYPE_CHOICE = [
        ('mobile', 'Мобильный'),
        ('desk', 'Стационарный'),
    ]
    type = models.CharField('Тип', max_length=50, choices=TYPE_CHOICE, default='mobile')
    phone = PhoneNumberField('Номер телефона')
    extension = models.CharField('Добавочный номер', max_length=20, blank=True)

    class Meta:
        abstract = True
