from flask import Blueprint, render_template, url_for

profile_blueprint = Blueprint(
        'profile', __name__,
        template_folder = 'templates'
        )

@profile_blueprint.route('/profile', methods=['POST', 'GET'])
def profile():
    """
    Profile 
    """
    return render_template('profile_index.html')

@profile_blueprint.route('/signupUser', methods=['POST', 'GET'])
def signupUser():
    user = request.form['username']
    password = request.form['password']
    return json.dump({'status':'OK', 'user':user, 'pass':password})
