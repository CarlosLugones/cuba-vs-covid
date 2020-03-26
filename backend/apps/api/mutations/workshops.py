import graphene

from apps.api.auth import authenticate
from apps.api.types.workshops import WorkshopType
from apps.core.models import Workshop, Address, City, Province


class CreateOrUpdateWorkshop(graphene.Mutation):
    status = graphene.String()
    workshop = graphene.Field(WorkshopType)

    class Arguments:
        name = graphene.String(required=True)
        phone = graphene.String(required=True)
        from_time = graphene.Time(required=True)
        to_time = graphene.Time(required=True)
        line_1 = graphene.String(required=True)
        line_2 = graphene.String()
        province = graphene.String(required=True)
        city = graphene.String(required=True)

    def mutate(self, info, name, phone, from_time, to_time, line_1, line_2, province, city):
        user = authenticate(info.context)

        if user is not None:

            city = City.objects.get(id=city)

            province = Province.objects.get(id=province)

            address = Address.objects.create(
                line_1=line_1,
                line_2=line_2,
                province=province,
                city=city
            )

            if user.workshop_set.count() == 0:

                workshop = Workshop.objects.create(
                    name=name,
                    phone=phone,
                    from_time=from_time,
                    to_time=to_time,
                    address=address,
                    owner=user
                )

            else:

                workshop = user.workshop_set.first()
                workshop.name = name
                workshop.phone = phone
                workshop.from_time = from_time
                workshop.to_time = to_time
                workshop.address = address
                workshop.save()

            return CreateOrUpdateWorkshop(status='ok', workshop=workshop)
        return CreateOrUpdateWorkshop(status='forbidden')
