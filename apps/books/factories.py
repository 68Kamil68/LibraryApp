import factory
from apps.core.publications.factories import PublicationFactory

from .models import Book


class BookFactory(PublicationFactory):
    class Meta:
        model = Book

    isbn = factory.Faker("isbn13")
    amount_of_pages = factory.Faker("pyint")
