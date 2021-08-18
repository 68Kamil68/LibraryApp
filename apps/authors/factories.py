import factory

from .models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    full_name = factory.Faker("name")
