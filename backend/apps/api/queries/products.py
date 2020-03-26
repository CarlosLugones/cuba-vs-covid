import graphene

from apps.api.auth import authenticate
from apps.api.types.workshops import WorkshopType


class ProductsQuery:
    viewer_products = graphene.Field(WorkshopType)

    def resolve_viewer_products(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.workshop_set.first()
        return None
