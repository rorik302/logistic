from django.contrib import admin

from payments.models import PaymentForm, PaymentTerm


@admin.register(PaymentForm)
class PaymentFormAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentTerm)
class PaymentTermAdmin(admin.ModelAdmin):
    pass
