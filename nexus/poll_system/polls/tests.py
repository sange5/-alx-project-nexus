from django.test import TestCase
from django.contrib.auth.models import User
from .models import Poll, Option, Vote

class PollModelTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(title="Best Programming Language")
        self.option1 = Option.objects.create(poll=self.poll, text="Python")
        self.option2 = Option.objects.create(poll=self.poll, text="JavaScript")

    def test_poll_creation(self):
        self.assertEqual(self.poll.title, "Best Programming Language")

    def test_option_creation(self):
        self.assertEqual(self.option1.text, "Python")
        self.assertEqual(self.option2.poll, self.poll)

class VoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.poll = Poll.objects.create(title="Best Framework")
        self.option = Option.objects.create(poll=self.poll, text="Django")
    
    def test_vote_creation(self):
        vote = Vote.objects.create(user=self.user, option=self.option)
        self.assertEqual(vote.user.username, "testuser")
