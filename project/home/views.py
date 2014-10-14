#################
#### imports ####
#################

from flask import render_template, Blueprint
from flask.ext.login import login_required

from project import db
from project.models import BlogPost

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
