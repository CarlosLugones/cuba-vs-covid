import graphene
from graphene_django.types import ObjectType

# Auth
from apps.api.mutations.auth import LoginMutation, RegisterMutation

# Users
from apps.api.queries.users import UserQuery
from apps.api.types.users import UserType

# Workshops
from apps.api.types.workshops import WorkshopType
from apps.api.queries.workshops import WorkshopQuery
from apps.api.mutations.workshops import CreateOrUpdateWorkshop

# Geo
from apps.api.types.geo import ProvinceType, CityType, AddressType
from apps.api.queries.geo import GeoQuery

# Products
from apps.api.types.products import ProductType
from apps.api.queries.products import ProductsQuery
from apps.api.mutations.products import CreateProduct


class Query(
    ObjectType,
    UserQuery,
    WorkshopQuery,
    GeoQuery,
    ProductsQuery
):
    pass


class Mutation(ObjectType):
    login = LoginMutation.Field()
    register = RegisterMutation.Field()
    create_or_update_workshop = CreateOrUpdateWorkshop.Field()
    create_product = CreateProduct.Field()


types = [
    UserType,
    WorkshopType,
    ProvinceType,
    CityType,
    AddressType,
    ProductType
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
