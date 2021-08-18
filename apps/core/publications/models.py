from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authors.models import Author
from apps.core.base.models import BaseModel


class Publication(BaseModel):
    authors = models.ManyToManyField(
        Author, related_name="%(class)ss", verbose_name=_("authors")
    )
    language = models.CharField(
        max_length=50, default="English", verbose_name=_("language")
    )
    publication_date = models.DateField(null=True, verbose_name=_("publication date"))
    title = models.CharField(max_length=200, verbose_name=_("title"))

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
