from graphene_django import DjangoObjectType

from backend.apps.core.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
