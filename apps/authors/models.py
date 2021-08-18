from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.base.models import BaseModel


class Author(BaseModel):
    full_name = models.TextField(verbose_name=_("full name"))
