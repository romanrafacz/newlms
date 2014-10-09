from flask import Blueprint, render_template

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
