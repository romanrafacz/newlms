#Instert models here
from __future__ import print_function

from app import db


class Location(db.Model):
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    facilityname = db.Column(db.String(120))
    facilityname2 = db.Column(db.String(150))
    address = db.Column(db.String(120))
    address2 = db.Column(db.String(120))
    city_state = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))
    phone = db.Column(db.String(120))

    def __unicode__(self):
        return self.facilityname

    def __repr__(self):
        return self.facilityname


class Instructor(db.Model):
    __tablename__ = "instructor"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(122))
    lastname = db.Column(db.String(122))
    email = db.Column(db.String(122))
    phone = db.Column(db.String(122))

    def __unicode__(self):
        return self.lastname
    

class Enrollments(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)
    coursecode = db.Column(db.String(8))
    trainingid = db.Column(db.String(10))
    startdate = db.Column(db.Date())
    enddate = db.Column(db.Date())
    location = db.Column(db.String(35))
    studentname = db.Column(db.String(50))
    studentemail = db.Column(db.String(50))
    phone = db.Column(db.String(12))
    trainingid = db.Column(db.String(12))

    def __unicode__(self):
        return self.coursecode

    def __repr__(self):
        return "<enrollment: (%s)" % (self.coursecode)
    
    

