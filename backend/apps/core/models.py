from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'core_user'

    def __str__(self):
        return str(self.username)


class Province(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'core_province'

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'core_city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Address(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'core_address'


class Workshop(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_workshop'


class STLModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='models')

    class Meta:
        db_table = 'core_stlmodel'


class Item(models.Model):
    name = models.CharField(max_length=255)
    stl_model = models.ForeignKey(STLModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_item'
