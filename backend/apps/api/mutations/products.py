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


class UpdateProduct(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        stock = graphene.Int(required=True)

    def mutate(self, info, id, name, stock):
        user = authenticate(info.context)
        if user is not None:
            try:
                product = Product.objects.get(pk=id)
                if product.owner == user:
                    product.name = name
                    product.stock = stock
                    product.save()
                    return UpdateProduct(status='ok')
            except Product.DoesNotExist:
                pass
        return UpdateProduct(status='forbidden')


class RemoveProduct(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        id = graphene.String(required=True)

    def mutate(self, info, id):
        user = authenticate(info.context)
        if user is not None:
            try:
                product = Product.objects.get(pk=id)
                if product.owner == user:
                    product.delete()
                    return RemoveProduct(status='ok')
            except Product.DoesNotExist:
                pass
        return RemoveProduct(status='forbidden')
