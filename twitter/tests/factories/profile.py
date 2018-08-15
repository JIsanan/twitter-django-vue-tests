import factory

from django.utils import timezone

from twitter.models import Profile
from twitter.tests.factories.auth import UserFactory


class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    fullname = factory.Faker('first_name')
    avatar_url = factory.Faker('first_name')
    created_at = factory.LazyFunction(timezone.now)
