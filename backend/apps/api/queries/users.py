import graphene

from apps.api.types.users import UserType
from apps.core.models import User


class UserQuery:
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
