from apps.core.publications.search_indexes import PublicationIndex
from haystack import indexes

from .models import Book


class BookIndex(PublicationIndex, indexes.Indexable):
    def get_model(self):
        return Book
