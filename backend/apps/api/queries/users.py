import graphene

from apps.api.types.users import UserType
from apps.api.auth import authenticate
from apps.core.models import User


class UserQuery:
    user = graphene.Field(UserType, id=graphene.Int())
    viewer_user = graphene.Field(UserType)

    def resolve_user(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_viewer_user(self, info):
        user = authenticate(info.context)
        return user
