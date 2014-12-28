#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint   # pragma: no cover
from flask.ext.login import login_user, \
    login_required, logout_user   # pragma: no cover

from .forms import LoginForm, RegisterForm   # pragma: no cover
from project import db   # pragma: no cover
from project.models import User, bcrypt   # pragma: no cover

################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   # pragma: no cover


################
#### routes ####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')   # pragma: no cover
@login_required   # pragma: no cover
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)
