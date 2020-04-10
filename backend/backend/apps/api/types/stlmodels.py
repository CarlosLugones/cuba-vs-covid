import graphene
from graphene_django import DjangoObjectType

from backend.apps.core.models import STLModel


class STLModelType(DjangoObjectType):
    stock = graphene.Int()

    class Meta:
        model = STLModel

    def resolve_stock(self, info):
        return self.stock
