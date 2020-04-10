from graphene_django import DjangoObjectType

from backend.apps.core.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
