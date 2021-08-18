import uuid

from django.db import models

from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(SoftDeletableModel, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
