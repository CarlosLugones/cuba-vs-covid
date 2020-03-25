import graphene
from graphql import GraphQLError
from django.contrib.auth.hashers import make_password

from apps.api.types.users import UserType
from apps.core.models import User


class RegisterMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    status = graphene.String()

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, first_name, last_name, email, password):
        try:
            if info.context.user.is_anonymous:
                try:
                    user = User.objects.get(email=email)
                    return RegisterMutation(status='already-registered')
                except User.DoesNotExist:
                    user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        username=email,
                        password=make_password(password),
                        is_active=True
                    )
                    return RegisterMutation(status='ok', user=user)
        except:
            raise GraphQLError(message='error')
