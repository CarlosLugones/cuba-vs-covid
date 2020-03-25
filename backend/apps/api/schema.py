import graphene
from graphene_django.types import ObjectType

from apps.api.queries.users import UserQuery
from apps.api.mutations.auth import RegisterMutation
from apps.api.types.users import UserType


class Query(
    ObjectType,
    UserQuery
):
    pass


class Mutation(ObjectType):
    register = RegisterMutation.Field()


types = [
    UserType
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
