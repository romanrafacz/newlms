from flask import render_template, Blueprint

schedule_blueprint = Blueprint(
        'schedule', __name__,
        template_folder = 'templates'
        )

@schedule_blueprint.route('/schedule')
def schedule():
    return "schedule page"
