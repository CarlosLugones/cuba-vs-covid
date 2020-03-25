import graphene
from graphene_django import DjangoObjectType

from apps.core.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
