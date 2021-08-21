from haystack import indexes

from .models import BaseModel


class BaseIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return BaseModel

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
