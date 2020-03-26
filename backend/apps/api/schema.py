import graphene
from graphene_django.types import ObjectType

from apps.api.queries.users import UserQuery
from apps.api.queries.workshops import WorkshopQuery
from apps.api.queries.geo import GeoQuery

from apps.api.mutations.auth import LoginMutation, RegisterMutation
from apps.api.mutations.workshops import CreateOrUpdateWorkshop

from apps.api.types.users import UserType
from apps.api.types.workshops import WorkshopType
from apps.api.types.geo import ProvinceType, CityType, AddressType


class Query(
    ObjectType,
    UserQuery,
    WorkshopQuery,
    GeoQuery
):
    pass


class Mutation(ObjectType):
    login = LoginMutation.Field()
    register = RegisterMutation.Field()

    create_or_update_workshop = CreateOrUpdateWorkshop.Field()


types = [
    UserType,
    WorkshopType,
    ProvinceType,
    CityType,
    AddressType
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
