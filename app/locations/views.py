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

@locations_blueprint.route('/locationinfo/<int:locationid>', methods=['POST', 'GET'])
def locationinfo(locationid):
    searchbylocation = db.session.query(Location).filter_by(id=locationid).first()
    return render_template('locationinfo.html', location=searchbylocation)
