import graphene
from graphql import GraphQLError
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from apps.api.types.users import UserType
from apps.core.models import User


class LoginMutation(graphene.Mutation):
    status = graphene.String()
    token = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        try:
            try:
                user = User.objects.get(email=email)
                if check_password(password=password, encoded=user.password) and user.is_active:
                    # Response without first_login
                    payload = jwt_payload_handler(user)
                    return LoginMutation(status='ok', token=jwt_encode_handler(payload), user=user)
            except User.DoesNotExist:
                pass
            return LoginMutation(status='error')
        except:
            raise GraphQLError(message='error')


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
