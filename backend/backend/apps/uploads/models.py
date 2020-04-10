import shutil
from django.db import models
from django.conf import settings

from backend.apps.core.models import HashModel, User


class TemporalUploadedFile(HashModel):
    url = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # ToDo: Add expiration datetime to auto delete orphan files

    class Meta:
        db_table = 'temporal_uploaded_file'

    def __str__(self):
        return self.url

    def move_to(self, new):
        old = '{}/{}'.format(settings.MEDIA_ROOT, self.url)
        shutil.move(old, new)
