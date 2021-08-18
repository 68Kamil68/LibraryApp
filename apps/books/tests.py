import pytest

from .factories import BookFactory
from .models import Book


@pytest.mark.django_db
def test_book_create():
    BookFactory()
    assert Book.objects.count() == 1
