import factory

from django.utils import timezone

from twitter.tests.factories.auth import UserFactory
from twitter.models import Tweet


class TweetFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tweet

    user = factory.SubFactory(UserFactory)
    content = factory.Faker('first_name')
    created_at = factory.LazyFunction(timezone.now)
