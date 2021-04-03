from django.contrib import admin

from companies.models import Company, CompanyType, Requisites


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Requisites)
class RequisitesAdmin(admin.ModelAdmin):
    pass
