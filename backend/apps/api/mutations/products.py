import graphene

from apps.api.auth import authenticate
from apps.api.types.products import ProductType
from apps.core.models import Product


class CreateProduct(graphene.Mutation):
    status = graphene.String()
    product = graphene.Field(ProductType)

    class Arguments:
        name = graphene.String(required=True)
        stock = graphene.Int(required=True)

    def mutate(self, info, name, stock):
        user = authenticate(info.context)

        if user is not None:
            product = Product.objects.create(name=name, stock=stock, owner=user)
            return CreateProduct(status='ok', product=product)
        return CreateProduct(status='forbidden')
