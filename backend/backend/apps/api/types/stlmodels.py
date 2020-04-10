from graphene_django import DjangoObjectType

from backend.apps.core.models import STLModel


class STLModelType(DjangoObjectType):
    class Meta:
        model = STLModel
