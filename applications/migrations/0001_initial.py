# Generated by Django 3.1.7 on 2021-04-03 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('outgoing_number', models.CharField(max_length=50, unique=True, verbose_name='Исходящий номер')),
                ('outgoing_date', models.DateField(verbose_name='Исходящая дата')),
                ('incoming_number', models.CharField(blank=True, max_length=50, verbose_name='Входящий номер')),
                ('incoming_date', models.DateField(blank=True, null=True, verbose_name='Входящая дата')),
                ('customer_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ставка заказчика')),
                ('transporter_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ставка перевозчику')),
                ('customer_penalties', models.TextField(verbose_name='Штрафные санкции с заказчиком')),
                ('transporter_penalties', models.TextField(verbose_name='Штрафные санкции с перевозчиком')),
                ('customer_additional_conditions', models.TextField(verbose_name='Дополнительные условия с заказчиком')),
                ('transporter_additional_conditions', models.TextField(verbose_name='Дополнительные условия с перевозчиком')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_applications', to='companies.company', verbose_name='Заказчик')),
                ('customer_payment_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_payment_form', to='payments.paymentform', verbose_name='Форма оплаты с заказчиком')),
                ('customer_payment_term', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_payment_term', to='payments.paymentterm', verbose_name='Срок оплаты с заказчиком')),
                ('own_company_with_customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='own_company_with_customer_applications', to='companies.company', verbose_name='Своя компанния с заказчиком')),
                ('own_company_with_transporter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='own_company_with_transporter_applications', to='companies.company', verbose_name='Своя компания с перевозчиком')),
                ('transporter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transporter_applications', to='companies.company', verbose_name='Перевозчик')),
                ('transporter_payment_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transporter_payment_form', to='payments.paymentform', verbose_name='Форма оплаты с перевозчиком')),
                ('transporter_payment_term', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transporter_payment_term', to='payments.paymentterm', verbose_name='Срок оплаты с перевозчиком')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'applications',
            },
        ),
    ]