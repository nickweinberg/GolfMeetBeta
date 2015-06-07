
import datetime
import unittest

from flask.ext.login import current_user

from base import BaseTestCase
from project import bcrypt
from project.models import User, ScoreCard
from project.user.forms import LoginForm


class TestScoreCardBlueprint(BaseTestCase):
    def test_create_new_scorecard(self):
        pass