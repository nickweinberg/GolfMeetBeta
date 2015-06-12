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

        # query database of User with id of user_id
        user = User.query.filter_by(id=user_id).first()
        # user.scorecards is list of all a User's scorecards
        # as_dict() is method on Scorecard model turns model
        # into something JSON serializable.
        results = [card.as_dict() for card in user.scorecards]

        return {'scorecards': results} # return json

    def post(self):
        # create new ScoreCard
        form = request.form

        # TODO: Add parser, depending on score format we settle on.
        parser = reqparse.RequestParser()
        parser.add_argument('scores', type=str, required=True, help='golf scores in string format')
        parser.add_argument('user_id', type=int, required=True, help='scorecard owner user id')

        args = parser.parse_args()

        user_id = current_user.id
        # new_scorecard = ScoreCard(
        #     scores=form['scores'],
        #     user_id=user_id
        # )

        new_scorecard = ScoreCard()
        new_scorecard.scores = args["scores"]
        new_scorecard.user_id = args["user_id"]

        try:
            db.session.add(new_scorecard)
            db.session.commit()
            print(new_scorecard.as_dict())
            return new_scorecard.as_dict(), 201

        except IntegrityError, exc:
            return {"error": exc.message}, 500

        # return success
        # return {'scorecard': marshal(new_scorecard, scorecard_fields)}, 201


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