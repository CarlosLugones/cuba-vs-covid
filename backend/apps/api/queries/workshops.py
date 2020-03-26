import graphene

from apps.api.auth import authenticate
from apps.api.types.workshops import WorkshopType


class WorkshopQuery:
    viewer_workshop = graphene.Field(WorkshopType)

    def resolve_viewer_workshop(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.workshop_set.first()
        return None
