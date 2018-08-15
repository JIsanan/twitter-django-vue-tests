from django.test import TestCase

from twitter.tests.factories.profile import ProfileFactory
from twitter.tests.factories.tweet import TweetFactory


class TweetModelTestCase(TestCase):
    def setUp(self):
        self.tweet = TweetFactory()

    def test_content(self):
        self.assertEqual(str(self.tweet), self.tweet.content)


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()

    def test_content(self):
        self.assertEqual(str(self.profile), self.profile.fullname)
