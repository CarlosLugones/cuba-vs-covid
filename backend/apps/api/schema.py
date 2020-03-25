import graphene
from graphene_django.types import ObjectType


class Query(ObjectType):
    pass


class Mutation(ObjectType):
    pass


schema = graphene.Schema()
