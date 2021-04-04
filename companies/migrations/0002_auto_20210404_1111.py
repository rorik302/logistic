# Generated by Django 3.1.7 on 2021-04-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name_full',
            field=models.CharField(max_length=255, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name_short',
            field=models.CharField(max_length=255, verbose_name='Сокращенное наименование'),
        ),
    ]
