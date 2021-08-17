import os

from django.db import models
from django.conf import settings

from model_utils.models import SoftDeletableModel, TimeStampedModel

from apps.authors.models import Author


class BaseModel(SoftDeletableModel, TimeStampedModel):
    class Meta:
        abstract = True


class Publication(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="%(class)ss",)
    language = models.CharField(max_length=50, default="Polish")
    publication_date = models.DateField(null=True)
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True


class WithThumbnail(models.Model):
    THUMBNAILS_STORAGE_PATH = os.path.join(settings.STORAGE_PATH, "thumbnails")

    thumbnail_url = models.URLField(null=True, blank=True)
    thumbnail = models.FileField(upload_to=THUMBNAILS_STORAGE_PATH, null=True)
