import graphene

from backend.apps.api.auth import authenticate
from backend.apps.api.types.products import ProductType
from backend.apps.core.models import Product, STLModel


class CreateProduct(graphene.Mutation):
    status = graphene.String()
    product = graphene.Field(ProductType)

    class Arguments:
        stlmodel = graphene.String(required=True)
        stock = graphene.Int(required=True)

    def mutate(self, info, stlmodel, stock):
        user = authenticate(info.context)

        if user is not None:
            model = STLModel.objects.get(pk=stlmodel)
            try:
                product = Product.objects.get(stlmodel=model, owner=user)
                product.stock += stock
                product.save()
            except Product.DoesNotExist:
                product = Product.objects.create(stlmodel=model, stock=stock, owner=user)
            return CreateProduct(status='ok', product=product)
        return CreateProduct(status='forbidden')


class UpdateProduct(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        id = graphene.String(required=True)
        stock = graphene.Int(required=True)

    def mutate(self, info, id, stock):
        user = authenticate(info.context)
        if user is not None:
            try:
                product = Product.objects.get(pk=id)
                if product.owner == user:
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
