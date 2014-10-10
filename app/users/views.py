from flask import Blueprint, render_template, redirect
from app.users.forms import UserLoginForm

users_blueprint = Blueprint(
        'users', __name__,
        template_folder = 'templates')

@users_blueprint.route('/users_login', methods=['POST', 'GET'])
def users_login():
    LoginForm = UserLoginForm()
    return render_template('users_index.html', form=LoginForm)
