from django.contrib import admin
from .models import TemporalUploadedFile


@admin.register(TemporalUploadedFile)
class TemporalUploadedFileAdmin(admin.ModelAdmin):
    fields = ('url', 'owner')
    list_display = fields
    readonly_fields = fields
