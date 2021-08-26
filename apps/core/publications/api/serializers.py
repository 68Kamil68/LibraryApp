from apps.authors.api.serializers import AuthorSerializer
from apps.core.publications.models import Publication
from apps.core.publications.search_indexes import PublicationIndex
from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers


class PublicationSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Publication
        fields = ["id", "language", "publication_date", "title", "authors"]


class PublicationHaystackSerializer(HaystackSerializer):
    class Meta:
        index_classes = [PublicationIndex]
        fields = ["authors", "language", "publication_date", "title"]
