from flask import render_template, Blueprint, request, url_for, flash, redirect, jsonify
from wtforms.ext.sqlalchemy.fields import QuerySelectField

##app objects
from app.models import Location
from app.locations.forms import LocationForm
from app import db


locations_blueprint = Blueprint(
        'locations', __name__,
        template_folder = "templates")

@locations_blueprint.route('/locations', methods=['POST', 'GET'])
def locations():
    """
    Location/Home - List all locations
    """
    Form = LocationForm()
    Form.state.choices = [(g.id, g.state) for g in Location.query.order_by('state')]
    ibmlocations = db.session.query(Location).all()
    return render_template('locations.html', locations=ibmlocations, form=Form)

@locations_blueprint.route('/searchbylocation/<int:locationid>', methods=['POST', 'GET'])
def searchbylocation(locationid):
    """
    Search by Location
    """
    searchbylocation = db.session.query(Location).filter_by(id=locationid).first()
    return render_template('searchbylocation.html', location=searchbylocation)

@locations_blueprint.route('/addlocation', methods=['POST', 'GET'])
def addlocation():
    """
     Add Location
    """
    message = ""
    if request.method == "POST":
        db.session.add(Location(location=request.form['location'], facilityname=request.form['facilityname'], address=request.form['address'], suite=request.form['suite'], city=request.form['city'], state=request.form['state'], zipcode=request.form['zipcode'], phone=request.form['phone']))
        db.session.commit()
        flash('successful add')
        return redirect('locations.html')
    else:
        flash("please try again")
        return redirect('locations.html')
    
    message= "no dice, try again"
    return render_template('addlocation.html', message=message)

@locations_blueprint.route('/editlocation', methods=['POST', 'GET'])
def editlocation():
    """
    Edit Location
    """

    #location = Location.query.get(1)
    Form = LocationForm()
    Form.state.choices = [(g.id, g.state) for g in Location.query.order_by('state')]
    return render_template('editlocations.html', form=Form)

def delete_location(locationid):
    """
    Function to delete location
    """
    db.session.query(Location).filter(Location.id==locationid).delete()
    db.session.commit()


@locations_blueprint.route('/deletelocation/<int:locationid>', methods=['POST', 'GET'])
def deletelocation(locationid):
    """
    Delete location
    """
    if delete_location(locationid):
        flash('deleted')
        return redirect('locations')
    else:
        flash('no can do')
        return redirect('locations')

@locations_blueprint.route('/_ajax_data')
def ajax_data():
    """
    Data to go into DataTables Template
    """
    #return jsonify({'draw':1, 'recordsTotal':1, "data":[[1, 'ATG', 'Atnta', 'AL', '708-299-7663', 'delete'],['2', 'CTS', 'chicago', 'IL', '708-299-7663', 'delete']] })
    #return jsonify({"data":['edit':1, 'location':'ATG', 'city':'Atlanta', 'state':'AL', 'phone':'708-299-7663', 'delete':'delete']})
    #return jsonify({'edit':1, 'location':'ATG', 'city':'Atlanta', 'state':'AL', 'phone':'708-299-7663', 'delete':'delete'})
    return jsonfiy(locations=(i.serialize for i in db.session.query(Locations).all()))
