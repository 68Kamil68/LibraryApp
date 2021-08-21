from apps.core.base.search_indexes import BaseIndex
from haystack import indexes

from .models import Publication


class PublicationIndex(BaseIndex):
    authors = indexes.MultiValueField(null=True, indexed=False)
    language = indexes.CharField(model_attr="language")
    publication_date = indexes.DateField(model_attr="publication_date", null=True)
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return Publication

    def prepare_authors(self, obj):
        return [author.full_name for author in obj.authors.all()]
