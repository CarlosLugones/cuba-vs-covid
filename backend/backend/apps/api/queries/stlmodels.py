import graphene

from backend.apps.api.types.stlmodels import STLModelType
from backend.apps.core.models import STLModel


class STLModelsQuery:
    stlmodels = graphene.List(STLModelType)
    existing_stlmodels = graphene.List(STLModelType)

    def resolve_stlmodels(self, info):
        return STLModel.objects.all()

    def resolve_existing_stlmodels(self, info):
        stlmodels = STLModel.objects.all()
        result = []
        for stlmodel in stlmodels:
            if stlmodel.stock > 0:
                result.append(stlmodel)
        return result
