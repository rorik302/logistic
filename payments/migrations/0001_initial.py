# Generated by Django 3.1.7 on 2021-04-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Форма оплаты',
                'verbose_name_plural': 'Формы оплат',
                'db_table': 'payment_forms',
            },
        ),
        migrations.CreateModel(
            name='PaymentTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('days_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество дней')),
                ('days_type', models.CharField(blank=True, choices=[('bank', 'банковские'), ('calendar', 'календарные')], max_length=50, verbose_name='Тип дней')),
                ('condition', models.CharField(max_length=255, verbose_name='Условия')),
            ],
            options={
                'verbose_name': 'Срок оплаты',
                'verbose_name_plural': 'Сроки оплат',
                'db_table': 'payment_terms',
            },
        ),
    ]
