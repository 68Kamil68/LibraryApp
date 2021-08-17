from django.db import models

from apps.core.models import BaseModel


class Author(BaseModel):
    full_name = models.TextField()
