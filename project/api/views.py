# project/api/views.py


#################
#### imports ####
#################

from flask import Blueprint, request
from flask_restful import Api, Resource, url_for, reqparse, abort

from flask.ext.login import login_required


from project import bcrypt, db
from project.models import User
from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo






################
#### config ####
################

api_blueprint = Blueprint('api', __name__,)
api = Api(api_blueprint)


####
# Forms Validation
####

# June 7th: not sure if best way to validate data is with forms.
class ScoreCardForm(Form):
    decorators = []
    scores = StringField(
        'Scores',
        validators=[DataRequired(), Length(min=6, max=25)])

################
### resources ##
################

class ExampleItem(Resource):
    def get(self, id):
        return {'example': 'Hello Whatever'}


class ScoreCardSimple(Resource):
    decorators = [login_required]

    def get(self, card_id):
        return {card_id: scorecards[card_id]}

    def put(self, card_id):
        scorecards[card_id] = request.form['data']
        return {card_id: scorecards[card_id]}




scorecards = {'1': '123'}
""" ScoreCard API
HTTP: URI
    - ACTION
GET : http://[hostname]/api/scorecards/[user_id]
    - Retrieves list of all user's scorecards

GET : http://[hostname]/api/scorecards/[user_id]/[scorecard_id]
    - Retrieves a ScoreCard

POST: http://[hostname]/api/scorecards/[user_id]
    - Create a new ScoreCard

PUT : http://[hostname]/api/scorecards/[user_id]/[scorecard_id]
    - Update an existing ScoreCard

DELETE: http://[hostname]/api/scorecards/[user_id]/[scorecard_id]
    - Delete a ScoreCard

*** Data Fields ***
URI: unique URI for ScoreCard. <String>
Date: DateTime Played. <String>


To Be Added:
Course: Name of Course. <String>
Users: ID of other users on this scorecard. (Not sure what type)


"""


api.add_resource(ExampleItem, '/example/<int:id>')
api.add_resource(ScoreCardSimple, '/scorecard/<int:user_id>/<string:card_id>')
