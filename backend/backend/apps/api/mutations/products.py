import graphene

from backend.apps.api.auth import authenticate
from backend.apps.api.types.products import ProductType
from backend.apps.core.models import Product


class CreateProduct(graphene.Mutation):
    status = graphene.String()
    product = graphene.Field(ProductType)

    class Arguments:
        name = graphene.String(required=True)
        stock = graphene.Int(required=True)
        photo = graphene.String()

    def mutate(self, info, name, stock, photo):
        user = authenticate(info.context)

        if user is not None:
            product = Product.objects.create(name=name, stock=stock, photo=photo, owner=user)
            return CreateProduct(status='ok', product=product)
        return CreateProduct(status='forbidden')


class UpdateProduct(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        stock = graphene.Int(required=True)
        photo = graphene.String()

    def mutate(self, info, id, name, stock, photo):
        user = authenticate(info.context)
        if user is not None:
            try:
                product = Product.objects.get(pk=id)
                if product.owner == user:
                    product.name = name
                    product.stock = stock
                    product.photo = photo
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
