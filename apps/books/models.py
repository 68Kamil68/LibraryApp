from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.publications.models import Publication, WithThumbnailMixin

from .validators import isbn_validator


class Book(Publication, WithThumbnailMixin):
    isbn = models.CharField(
        max_length=20, validators=[isbn_validator], verbose_name=_("isbn number")
    )
    amount_of_pages = models.IntegerField(verbose_name=_("amount of pages"))
