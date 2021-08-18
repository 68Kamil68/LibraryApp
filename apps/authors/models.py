from django.db import models

from apps.core.base.models import BaseModel


class Author(BaseModel):
    full_name = models.TextField()
