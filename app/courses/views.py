from flask import render_template, Blueprint

courses_blueprint = Blueprint(
        'courses', __name__,
        template_folder='templates'
        )

@courses_blueprint.route('/courses')
def courses():
    return render_template('courses.html')
