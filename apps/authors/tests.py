import pytest

from .factories import AuthorFactory
from .models import Author


@pytest.mark.django_db
def test_author_create():
    AuthorFactory()
    assert Author.objects.count() == 1
