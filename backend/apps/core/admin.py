from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    pass


@admin.register(models.STLModel)
class STLModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
