import graphene

from apps.api.auth import authenticate
from apps.api.types.workshops import WorkshopType


class WorkshopQuery:
    viewer_workshops = graphene.List(WorkshopType)

    def resolve_viewer_workshops(self, info):
        user = authenticate(info.context)
        if user is not None:
            return user.workshop_set.all()
        return None
