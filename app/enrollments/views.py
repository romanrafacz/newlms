from flask import render_template, Blueprint

enrollments_blueprint = Blueprint(
        'enrollments', __name__,
        template_folder = 'templates'
        )

@enrollments_blueprint.route('/enrollments')
def enrollments():
    return render_template('index.html')

