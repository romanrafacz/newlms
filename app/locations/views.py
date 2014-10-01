from flask import render_template, Blueprint, request, url_for, flash

from app.models import Location
from app.locations.forms import LocationForm

from app import db

locations_blueprint = Blueprint(
        'locations', __name__,
        template_folder = "templates")

@locations_blueprint.route('/locations', methods=['POST', 'GET'])
def locations():
    Form = LocationForm()
    ibmlocations = db.session.query(Location).all()
    return render_template('locations.html', locations=ibmlocations, form=Form)

@locations_blueprint.route('/searchbylocation/<int:locationid>', methods=['POST', 'GET'])
def searchbylocation(locationid):
    searchbylocation = db.session.query(Location).filter_by(id=locationid).first()
    return render_template('searchbylocation.html', location=searchbylocation)

@locations_blueprint.route('/addlocation', methods=['POST', 'GET'])
def addlocation():
    message = ""
    if request.method == "POST":
        db.session.add(Location(facilityname=request.form['facilityname'], facilityname2=request.form['facilityname2'], address=request.form['address'], address2=request.form['address2'], city=request.form['city'], state=request.form['state'], zipcode=request.form['zipcode'], phone=request.form['phone']))
        db.session.commit()
        flash('successful add')
        return render_template('addlocation.html')
    else:
        flash("please try again")
        return render_template('locations.html')
    
    message= "no dice, try again"
    return render_template('addlocation.html', message=message)

@locations_blueprint.route('/editlocation', methods=['POST', 'GET'])
def editlocation():
    Form = LocationForm()
    locationdata = db.session.query(Location).filter(id==1).all()
    Form.populate_obj(locationdata)
    return render_template('editlocations.html', form=Form)
