import graphene

from backend.apps.api.auth import authenticate
from backend.apps.api.types.stlmodels import STLModelType
from backend.apps.core.models import STLModel


class STLModelsQuery:
    stlmodels = graphene.List(STLModelType)

    def resolve_stlmodels(self, info):
        return STLModel.objects.all()
