import graphene

from backend.apps.api.auth import authenticate
from backend.apps.api.types.users import UserType
from backend.apps.core.models import Address, City, Province


class UpdateUser(graphene.Mutation):
    status = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone = graphene.String(required=True)
        from_time = graphene.Time(required=True)
        to_time = graphene.Time(required=True)
        line_1 = graphene.String(required=True)
        line_2 = graphene.String()
        province = graphene.String(required=True)
        city = graphene.String(required=True)

    def mutate(self, info, first_name, last_name, phone, from_time, to_time, line_1, line_2, province, city):
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

            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.from_time = from_time
            user.to_time = to_time
            user.address = address
            user.save()

            return UpdateUser(status='ok', user=user)
        return UpdateUser(status='forbidden')
