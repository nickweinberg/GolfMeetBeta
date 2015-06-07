# project/api/views.py


#################
#### imports ####
#################

from flask import Blueprint, request
from flask_restful import Api, Resource, url_for


################
#### config ####
################

api_blueprint = Blueprint('api', __name__,)
api = Api(api_blueprint)


################
### resources ##
################

class ExampleItem(Resource):
    def get(self, id):
        return {'example': 'Hello Whatever'}


class ScoreCardSimple(Resource):
    def get(self, card_id):
        return {card_id: scorecards[card_id]}

    def put(self, card_id):
        scorecards[card_id] = request.form['data']
        return {card_id: scorecards[card_id]}


scorecards = {'1': '123'}



api.add_resource(ExampleItem, '/example/<int:id>')
api.add_resource(ScoreCardSimple, '/scorecard/<string:card_id>')
