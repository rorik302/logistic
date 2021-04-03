from django.contrib import admin

from drivers.models import Driver, DriverPhone, DriverLicense, DriverPassport


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverPhone)
class DriverPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverPassport)
class DriverPassportAdmin(admin.ModelAdmin):
    pass
