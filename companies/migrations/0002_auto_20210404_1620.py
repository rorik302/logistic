# Generated by Django 3.1.7 on 2021-04-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisites',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активно'),
        ),
        migrations.AddField(
            model_name='requisites',
            name='slug',
            field=models.CharField(blank=True, max_length=50, verbose_name='Слаг'),
        ),
    ]
