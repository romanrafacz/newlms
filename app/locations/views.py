from flask import render_template, Blueprint

locations_blueprint = Blueprint(
        'locations', __name__,
        template_folder = "templates")

@locations_blueprint.route('/locations')
def locations():
    return "locations page"
