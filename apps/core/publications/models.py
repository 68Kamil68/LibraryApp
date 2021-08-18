from django.db import models

from apps.authors.models import Author
from apps.core.base.models import BaseModel


class Publication(BaseModel):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="%(class)ss",
    )
    language = models.CharField(max_length=50, default="Polish")
    publication_date = models.DateField(null=True)
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True


class WithThumbnailMixin(models.Model):
    THUMBNAILS_STORAGE_PATH = "thumbnails"

    thumbnail_url = models.URLField(null=True, blank=True)
    thumbnail = models.FileField(
        upload_to=THUMBNAILS_STORAGE_PATH, null=True, blank=True
    )

    class Meta:
        abstract = True
