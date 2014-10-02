from flask import render_template, Blueprint, request, url_for, flash, redirect

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
        db.session.add(Location(location=request.form['location'], facilityname=request.form['facilityname'], address=request.form['address'], suite=request.form['suite'], city=request.form['city'], state=request.form['state'], zipcode=request.form['zipcode'], phone=request.form['phone']))
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
    locationdata = Location.query.get(1)
    Form.populate_obj(request.POST, locaitondata)
    return render_template('editlocations.html', form=Form)


@locations_blueprint.route('/deletelocation/<int:locationid>', methods=['POST', 'GET'])
def deletelocation(locationid):
    db.session.query(Location).filter(Location.id==locationid).delete()
    db.session.commit()
    return redirect('locations')
