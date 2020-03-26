from graphene_django import DjangoObjectType

from apps.core.models import Workshop


class WorkshopType(DjangoObjectType):
    class Meta:
        model = Workshop
