import graphene
from graphene_django.types import ObjectType

# Auth
from backend.apps.api.mutations.auth import LoginMutation, RegisterMutation

# Users
from backend.apps.api.types.users import UserType
from backend.apps.api.queries.users import UserQuery
from backend.apps.api.mutations.users import UpdateUser

# Geo
from backend.apps.api.types.geo import ProvinceType, CityType, AddressType
from backend.apps.api.queries.geo import GeoQuery

# Products
from backend.apps.api.types.products import ProductType
from backend.apps.api.queries.products import ProductsQuery
from backend.apps.api.mutations.products import CreateProduct, UpdateProduct, RemoveProduct


class Query(
    ObjectType,
    UserQuery,
    GeoQuery,
    ProductsQuery
):
    pass


class Mutation(ObjectType):
    # auth
    login = LoginMutation.Field()
    register = RegisterMutation.Field()

    # users
    update_user = UpdateUser.Field()

    # products
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    remove_product = RemoveProduct.Field()


types = [
    UserType,
    ProvinceType,
    CityType,
    AddressType,
    ProductType
]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
