import graphene

from backend.apps.api.auth import authenticate
from backend.apps.api.types.products import ProductType
from backend.apps.core.models import Product, Province, City, STLModel


class ProductsQuery:
    product = graphene.Field(ProductType, id=graphene.String(required=True))
    viewer_products = graphene.List(ProductType)
    filter_products = graphene.List(
        ProductType,
        stlmodel=graphene.String(required=True),
        province=graphene.String(),
        city=graphene.String()
    )

    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)

    def resolve_viewer_products(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.product_set.all()
        return None

    def resolve_filter_products(self, info, stlmodel, province=None, city=None):

        model = STLModel.objects.get(pk=stlmodel)

        kwargs = {
            'stlmodel': model
        }

        if province is not None:
            # Get province
            try:
                province = Province.objects.get(pk=province)
                kwargs['owner__address__province'] = province
            except Province.DoesNotExist:
                pass

        if city is not None:
            # Get city
            try:
                city = City.objects.get(pk=city)
                kwargs['owner__address__city'] = city
            except City.DoesNotExist:
                pass

        return Product.objects.filter(**kwargs)
