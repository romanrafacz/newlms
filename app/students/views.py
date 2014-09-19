from flask import render_template, Blueprint

students_blueprint = Blueprint(
        'students', __name__,
        template_folder = "templates"
        )

@students_blueprint.route('/students')
def students():
    return "students page"

