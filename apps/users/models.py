from django.contrib.auth.models import AbstractUser

from apps.core.base.models import BaseModel


class User(AbstractUser, BaseModel):
    pass
