import factory
from apps.authors.factories import AuthorFactory

from .models import Publication


class PublicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publication

    author = factory.SubFactory(AuthorFactory)
    language = factory.Faker("language_name")
    publication_date = factory.Faker("past_date")
    title = factory.Faker("sentence", nb_words=3)
