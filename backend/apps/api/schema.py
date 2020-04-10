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
from apps.api.mutations.products import CreateProduct, UpdateProduct


class Query(
    ObjectType,
    UserQuery,
    WorkshopQuery,
    GeoQuery,
    ProductsQuery
):
    pass


class Mutation(ObjectType):
    # auth
    login = LoginMutation.Field()
    register = RegisterMutation.Field()

    # workshop
    create_or_update_workshop = CreateOrUpdateWorkshop.Field()

    # products
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()


types = [
    UserType,
    WorkshopType,
    ProvinceType,
    CityType,
    AddressType,
    ProductType
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
