
import datetime
import unittest

from flask.ext.login import current_user

from base import BaseTestCase
from project import bcrypt
from project.models import User, ScoreCard
from project.user.forms import LoginForm

"""

curl -i -X POST -H "Content-Type: application/json" -d '{"scores":"12-23-995-22"}' http://127.0.0.1:5000/api/scorecards


"""


class TestScoreCardBlueprint(BaseTestCase):
    def test_create_new_scorecard(self):
        # Ensure registration behaves correctlys.

        with self.client:
            # login first
            self.client.post('/login', data=dict(
                email='ad@min.com', password='admin_user'
            ))

            response = self.client.post(
                '/api/scorecards',
                data=dict(scores="1-1-2-3-4-1-1"),
                headers={'content-type':'application/json'}
            )

        self.assertEqual(response.status_code, 201)

    def test_create_scorecard_no_scores(self):

        with self.client:
            # login first
            self.client.post('/login', data=dict(
                email='ad@min.com', password='admin_user'
            ), follow_redirects=True)

            response = self.client.post(
                '/api/scorecards',
                data=dict()
            )

        self.assert400(response)


