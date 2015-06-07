# project/scorecard/views.py


from flask import render_template, Blueprint


#################
#### imports ####
#################

from flask import render_template, Blueprint

from flask.ext.login import login_required

from project import bcrypt, db
from project.models import User
from project.user.forms import LoginForm, RegisterForm

################
#### config ####
################

scorecard_blueprint = Blueprint('scorecard', __name__,)


################
#### routes ####
################


@scorecard_blueprint.route('/scorecards/all')
@login_required
def scorecard_main():
    return render_template('scorecard/scorecards.html')

