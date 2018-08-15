import factory.django

from django.contrib.auth.models import User

import uuid


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = str(uuid.uuid4())
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password')
