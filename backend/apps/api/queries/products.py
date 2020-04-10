import graphene

from apps.api.auth import authenticate
from apps.api.types.products import ProductType
from apps.core.models import Product


class ProductsQuery:
    product = graphene.Field(ProductType, id=graphene.String(required=True))
    viewer_products = graphene.List(ProductType)

    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)

    def resolve_viewer_products(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.product_set.all()
        return None
