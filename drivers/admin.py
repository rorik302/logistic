from django.contrib import admin

from drivers.models import Driver, DriverPhone, DriverLicense, DriverPassport


class DriverPhoneInline(admin.StackedInline):
    model = DriverPhone
    extra = 0


class DriverPassportInline(admin.StackedInline):
    model = DriverPassport
    extra = 0


class DriverLicenseInline(admin.StackedInline):
    model = DriverLicense
    extra = 0


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    inlines = [DriverPhoneInline, DriverPassportInline, DriverLicenseInline]


@admin.register(DriverPhone)
class DriverPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverPassport)
class DriverPassportAdmin(admin.ModelAdmin):
    pass
