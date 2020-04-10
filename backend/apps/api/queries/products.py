import graphene

from apps.api.auth import authenticate
from apps.api.types.products import ProductType


class ProductsQuery:
    viewer_products = graphene.List(ProductType)

    def resolve_viewer_products(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.product_set.all()
        return None
