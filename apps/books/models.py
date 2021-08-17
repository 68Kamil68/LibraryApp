from django.db import models

from apps.core.models import Publication, WithThumbnail

from .validators import isbn_validator


class Book(Publication, WithThumbnail):
    isbn = models.CharField(max_length=20, validators=[isbn_validator])
    number_of_pages = models.IntegerField()

