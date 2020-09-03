from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from models.user import User, UserErrors
import re

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            session['email'] = email
            return redirect(url_for('alerts.index'))

        except UserErrors.UserError as e:
            flash('We already have you in the system, log in below!', 'warning')
            return redirect(url_for('users.login_user'))

    return render_template('users/register.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                pattern = re.compile(r"^.*(?=(@))")
                match = pattern.search(email)
                name = match.group(0)
                flash('Welcome back, {}!'.format(name), 'success')
                return redirect(url_for('alerts.index'))
        except UserErrors.IncorrectPasswordError as e:
            flash(e.message, 'danger')
        except:
            flash("Looks like you're not registered yet, do it now!", 'warning')
            return redirect(url_for('users.register_user'))

    return render_template('users/login.html')

@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    flash("See you later!", 'success')
    return redirect(url_for('users.login_user'))
