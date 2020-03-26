import graphene
from graphene_django import DjangoObjectType

from apps.core.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
