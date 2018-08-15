from django.test import TestCase

from twitter.tests.factories.auth import UserFactory
from twitter.tests.factories.profile import ProfileFactory
from twitter.tests.factories.tweet import TweetFactory

from twitter.serializers import (
    TweetSerializer,
    ProfileSerializer,
    UserSerializer
)


class TweetTestCase(TestCase):
    def setUp(self):
        self.tweet = TweetFactory()

    def test_tweet_length(self):
        string_val = "x" * 240
        form = TweetSerializer(data={
            'created_at': self.tweet.created_at,
            'content': string_val,
            'user': self.tweet.user})
        self.assertTrue(form.is_valid())
        string_val = "x" * 1000
        form = TweetSerializer(data={
            'created_at': self.tweet.created_at,
            'content': string_val,
            'user': self.tweet.user})
        self.assertFalse(form.is_valid())
        string_val = "x" * 0
        form = TweetSerializer(data={
            'created_at': self.tweet.created_at,
            'content': string_val,
            'user': self.tweet.user})
        self.assertFalse(form.is_valid())

    def test_tweet_no_content(self):
        form = TweetSerializer(data={
            'created_at': self.tweet.created_at,
            'user': self.tweet.user})
        self.assertFalse(form.is_valid())

    def test_tweet_perform_create(self):
        form = TweetSerializer(data={
            'created_at': self.tweet.created_at,
            'content': 'wasadfsadf'})
        form.is_valid()
        form.save(user=self.tweet.user)
        self.assertTrue(form)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()

    def test_profile_fullname_length(self):
        string_val = "x" * 240
        form = ProfileSerializer(data={
            'fullname': string_val,
            'user': self.profile.user})
        self.assertTrue(form.is_valid())
        string_val = "x" * 1000
        form = ProfileSerializer(data={
            'fullname': string_val,
            'user': self.profile.user})
        self.assertFalse(form.is_valid())
        string_val = "x" * 0
        form = ProfileSerializer(data={
            'fullname': string_val,
            'user': self.profile.user})
        self.assertFalse(form.is_valid())


class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()

    def test_username_length(self):
        string_val = "x" * 10
        form = UserSerializer(data={
            'username': string_val,
            'email': self.user.email})
        self.assertTrue(form.is_valid())
        string_val = "x" * 1000
        form = UserSerializer(data={
            'fullname': string_val,
            'email': self.user.email})
        self.assertFalse(form.is_valid())
        string_val = "x" * 0
        form = UserSerializer(data={
            'fullname': string_val,
            'email': self.user.email})
        self.assertFalse(form.is_valid())

    def test_username_equal(self):
        string_val = "x" * 10
        form = UserSerializer(data={
            'username': string_val,
            'email': self.user.email})
        form.is_valid()
        string_val = "x" * 10
        form = UserSerializer(data={
            'fullname': string_val,
            'email': self.user.email})
        self.assertFalse(form.is_valid())

    def test_email_length(self):
        string_val = "x" * 10 + '@smthn.com'
        form = UserSerializer(data={
            'username': self.user.username + 'aa',
            'email': string_val})
        self.assertTrue(form.is_valid())
        string_val = "x" * 1000 + '@smthn.com'
        form = UserSerializer(data={
            'username': self.user.username + 'aaa',
            'email': string_val})
        self.assertFalse(form.is_valid())
        string_val = "x" * 0 + '@smthn.com'
        form = UserSerializer(data={
            'username': self.user.username + 'a',
            'email': string_val})
        self.assertFalse(form.is_valid())

    def test_email_invalid(self):
        string_val = "x" * 10
        form = UserSerializer(data={
            'username': self.user.username + 'b',
            'email': string_val})
        self.assertFalse(form.is_valid())
