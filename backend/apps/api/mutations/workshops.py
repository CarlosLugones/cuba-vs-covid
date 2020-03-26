import graphene

from apps.api.auth import authenticate
from apps.api.types.workshops import WorkshopType
from apps.core.models import Workshop, Address, City, Province


class CreateWorkshop(graphene.Mutation):
    status = graphene.String()
    workshop = graphene.Field(WorkshopType)

    class Arguments:
        name = graphene.String(required=True)
        phone = graphene.String(required=True)
        from_time = graphene.Time(required=True)
        to_time = graphene.Time(required=True)
        address_line_1 = graphene.String(required=True)
        address_line_2 = graphene.String()
        address_province = graphene.String(required=True)
        address_city = graphene.String(required=True)

    def mutate(self, info, name, phone, from_time, to_time, address_line_1, address_line_2, address_province, address_city):
        user = authenticate(info.context)
        if user is not None:
            city = City.objects.get(id=address_city)
            province = Province.objects.get(id=address_province)
            address = Address.objects.create(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                province=province,
                city=city
            )
            workshop = Workshop.objects.create(
                name=name,
                phone=phone,
                from_time=from_time,
                to_time=to_time,
                address=address,
                owner=user
            )
            return CreateWorkshop(status='ok', workshop=workshop)
        return CreateWorkshop(status='forbidden')
