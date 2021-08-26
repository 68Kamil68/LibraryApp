from apps.authors.models import Author
from apps.books.models import Book
from apps.books.search_indexes import BookIndex
from apps.core.publications.api.serializers import (
    PublicationHaystackSerializer,
    PublicationSerializer,
)


class BookSerializer(PublicationSerializer):
    class Meta:
        model = Book
        fields = PublicationSerializer.Meta.fields + ["isbn", "amount_of_pages"]

    def create(self, validated_data):
        authors_data = validated_data.pop("authors")
        book_instance = super().create(validated_data)
        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(**author_data)
            book_instance.authors.add(author)
        return book_instance


class BookHaystackSerializer(PublicationHaystackSerializer):
    class Meta:
        index_classes = [BookIndex]
        fields = PublicationHaystackSerializer.Meta.fields
