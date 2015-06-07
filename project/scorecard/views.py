# project/scorecard/views.py


from flask import render_template, Blueprint


#################
#### imports ####
#################

from flask import render_template, Blueprint


################
#### config ####
################

scorecard_blueprint = Blueprint('scorecard', __name__,)


################
#### routes ####
################


@scorecard_blueprint.route('/scorecards')
def home():
    return render_template('scorecard/index.html')
