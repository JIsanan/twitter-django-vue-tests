from django.test import TestCase, Client

from twitter.tests.factories.auth import UserFactory
from twitter.tests.factories.profile import ProfileFactory
from twitter.tests.factories.tweet import TweetFactory
from twitter.models import Tweet
from django.contrib.auth.models import User

from twitter.serializers import (
    TweetSerializer,
    ProfileSerializer,
    UserSerializer
)

from rest_framework import status

client = Client()


class RegisterViewTestCase(TestCase):

    def test_api_view(self):
        response = client.get('/api/')
        self.assertEqual(response.status_code, 200)


class CurrentUserViewTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()
        self.profile.user.set_password('rolo')
        self.profile.user.save()
        data = {
            'username': self.profile.user.username,
            'password': 'rolo'
        }
        response = self.client.post('/api-token-auth/', data, format='json')
        self.token = response.data['token']

    def test_api_view(self):
        response = self.client.get(
            '/api/me/',
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            format='json'
        )
        self.assertEqual(response.status_code, 200)


class UserTweetsViewTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()
        self.profile.user.set_password('rolo')
        self.profile.user.save()
        data = {
            'username': self.profile.user.username,
            'password': 'rolo'
        }
        response = self.client.post('/api-token-auth/', data, format='json')
        self.token = response.data['token']

    def test_user_tweets_view(self):
        response = self.client.get(
            '/api/users/' + self.profile.user.username + '/tweets/',
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            format='json'
        )
        self.assertEqual(response.status_code, 200)


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()
        self.profile.user.set_password('rolo')
        self.profile.user.save()
        data = {
            'username': self.profile.user.username,
            'password': 'rolo'
        }
        response = self.client.post('/api-token-auth/', data, format='json')
        self.token = response.data['token']

    def test_user_profile_view(self):
        response = self.client.get(
            '/api/users/' + self.profile.user.username + '/',
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            format='json'
        )
        self.assertEqual(response.status_code, 200)


class RegisterTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()
        self.profile.user.set_password('rolo')
        self.profile.user.save()

    def test_register(self):
        response = self.client.post(
            '/api-auth/register/', {
                'username': 'bbossafsdvival',
                'email': 'bbsadasd@ssm.com',
                'password': 'random123',
                'fullname': 'rensfsdf',
            }
        )
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            '/api-auth/register/', {
                'username': 'bbossafsdvival',
                'email': 'bbsadasd@ssm.com',
                'password': 'random123',
                'fullname': 'rensfsdf',
            }
        )
        self.assertEqual(response.status_code, 400)
        response = self.client.post(
            '/api-auth/register/', {
                'username': 'bbossafsdvival',
                'fullname': 'rensfsdf',
            }
        )
        self.assertEqual(response.status_code, 400)


class TweetViewSetTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()
        self.profile.user.set_password('rolo')
        self.profile.user.save()
        data = {
            'username': self.profile.user.username,
            'password': 'rolo'
        }
        response = self.client.post('/api-token-auth/', data, format='json')
        self.token = response.data['token']

    def test_register(self):
        response = self.client.post(
            '/api/tweets/', {
                'content': 'wasadfsadf'
            },
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            '/api/tweets/', {
            },
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            format='json'
        )
        self.assertEqual(response.status_code, 400)
