import graphene

from backend.apps.api.types.geo import ProvinceType, CityType
from backend.apps.core.models import Province, City


class GeoQuery:
    provinces = graphene.List(ProvinceType)
    cities = graphene.List(CityType, province_id=graphene.String())

    def resolve_provinces(self, info):
        return Province.objects.all()

    def resolve_cities(self, info, province_id):
        return City.objects.filter(province=province_id)
