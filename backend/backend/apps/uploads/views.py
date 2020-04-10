from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from rest_framework import status

from backend.apps.api.auth import authenticate
from backend.apps.uploads.models import TemporalUploadedFile


@require_POST
def upload(request):
    user = authenticate(request)
    if user is not None:
        try:
            extension = '.' + request.POST['format']
            file = request.FILES['file']
            temporal = TemporalUploadedFile.objects.create(owner=user)
            url = '{}.{}'.format(temporal.hash, extension)
            location = '{}/{}'.format(
                settings.MEDIA_ROOT,
                url
            )
            temporal.url = url
            temporal.save()
            with open(location, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return JsonResponse(data={'url': url}, status=status.HTTP_200_OK)
        except KeyError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)
