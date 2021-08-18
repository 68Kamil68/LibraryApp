from django.db import models

from apps.core.publications.models import Publication, WithThumbnailMixin

from .validators import isbn_validator


class Book(Publication, WithThumbnailMixin):
    isbn = models.CharField(max_length=20, validators=[isbn_validator])
    amount_of_pages = models.IntegerField()
