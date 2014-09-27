from flask import render_template, Blueprint

from app.locations.models import Location

from app import db

locations_blueprint = Blueprint(
        'locations', __name__,
        template_folder = "templates")

@locations_blueprint.route('/locations')
def locations():
    ibmlocations = db.session.query(Location).all()
    return render_template('locations.html', locations=ibmlocations)
