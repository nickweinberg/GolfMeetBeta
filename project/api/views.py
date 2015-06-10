# project/api/views.py


#################
#### imports ####
#################

from flask import Blueprint, request, session, g
from flask_restful import Api, Resource, url_for, reqparse, abort, fields, marshal

from flask.ext.login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from project import bcrypt, db
from project.models import User, ScoreCard

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

scorecard_fields = {
   'scores': fields.String,
   'user_id': fields.Integer,
   'uri': fields.Url('scorecard')
}

class ScoreCardListAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument()

    def get(self):
        # get all scorecards
        user_id = current_user.id

        user = User.query.filter_by(id=user_id).first()
        all_scorecards = user.scorecards

        return {'scorecards': all_scorecards}

    def post(self):
        # create new ScoreCard
        form = request.form

        # TODO: Add parser, depending on score format we settle on.
        user_id = current_user.id
        new_scorecard = ScoreCard(
            scores=form['scores'],
            user_id=user_id
        )
        try:
            db.session.add(new_scorecard)
            db.session.commit()
        except IntegrityError, exc:
            return {"error": exc.message}, 500

        # return success
        return {'scorecard': marshal(new_scorecard, scorecard_fields)}, 201


class ScoreCardAPI(Resource):
    decorators = [login_required]

    def get(self, card_id):
        user_id = current_user.id
        return {'example': str(user_id) + ' ' + str(card_id)}



    def put(self, card_id):
        pass

    def delete(self, card_id):
        pass



api.add_resource(ScoreCardListAPI, '/api/scorecards', endpoint="scorecard_list")
api.add_resource(ScoreCardAPI, '/api/scorecards/<int:card_id>', endpoint="scorecard")