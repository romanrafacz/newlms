from flask import Blueprint, render_template, redirect, url_for, request
from app.users.forms import UserLoginForm

users_blueprint = Blueprint(
        'users', __name__,
        template_folder = 'templates')

@users_blueprint.route('/users_login', methods=['POST', 'GET'])
def users_login():
    LoginForm = UserLoginForm()

    if request.method == 'GET':
        return render_template('users_index.html', form=LoginForm)
    username = request.form['username']
    password = request.form['password']
    return redirect(request.args.get('next') or url_for('app.locations.locations'))
