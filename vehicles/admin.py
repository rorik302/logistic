from django.contrib import admin

from vehicles.models import Vehicle, VehicleParameters


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(VehicleParameters)
class VehicleParametersAdmin(admin.ModelAdmin):
    pass
