from graphene_django import DjangoObjectType

from apps.core.models import Province, City, Address


class ProvinceType(DjangoObjectType):
    class Meta:
        model = Province


class CityType(DjangoObjectType):
    class Meta:
        model = City


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
