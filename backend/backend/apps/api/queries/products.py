import graphene

from backend.apps.api.auth import authenticate
from backend.apps.api.types.products import ProductType
from backend.apps.core.models import Product


class ProductsQuery:
    product = graphene.Field(ProductType, id=graphene.String(required=True))
    viewer_products = graphene.List(ProductType)
    existing_products = graphene.List(ProductType)

    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)

    def resolve_viewer_products(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.product_set.all()
        return None

    def resolve_existing_products(self, info):
        return Product.objects.filter(stock__gt=0)
