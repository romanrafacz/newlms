#Instert models here
from __future__ import print_function

from app import db


class Location(db.Model):
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(120))
    facilityname = db.Column(db.String(150))
    address = db.Column(db.String(120))
    suite = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))
    phone = db.Column(db.String(120))
    location = db.relationship("Schedule", backref='location')

    def __unicode__(self):
        return self.facilityname

    def __repr__(self):
        return self.facilityname

    @property
    def serialize(self):
        return {
            'location': self.location,
            'facilityname': self.facilityname,
            'address' : self.address,
            'suite' : self.suite,
            'city' : self.city,
            'state' : self.city,
            'zipcode' : self.zipcode,
            'phone' : self.phone
        }


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

    enrollment_id = db.Column(db.Integer, primary_key=True)
    coursecode = db.Column(db.String(8))
    training_id = db.Column(db.String(10))
    startdate = db.Column(db.Date())
    enddate = db.Column(db.Date())
    location = db.Column(db.String(100))
    student_id = db.Column(db.String(100))
    student_name = db.Column(db.String(50))
    student_email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    price = db.Column(db.String(10))
    status = db.Column(db.String(15))

    def __unicode__(self):
        return self.coursecode

    def __repr__(self):
        return "<enrollment: (%s)" % (self.coursecode)

class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    comments = db.Column(db.Text)

class Course(db.Model):
    __tablename__ = "course"

    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coursecode = db.Column(db.String(6), unique=True)
    coursename = db.Column(db.String(120))
    price = db.Column(db.String(10))
    duration = db.Column(db.String(10))
    category = db.Column(db.String(250))
    #schedule = db.relationship("Schedule", lazy="joined", backref="course")

    def __unicode__(self):
        return self.coursecode

class Schedule(db.Model):
    __tablename__ = "schedule"

    scheduleid = db.Column(db.Integer, primary_key=True)
    locationid = db.Column(db.Integer, db.ForeignKey('location.id'))
    coursecode = db.Column(db.String(6), db.ForeignKey('course.coursecode'))
    startdate = db.Column(db.Date())
    enddate = db.Column(db.Date())

    def __unicode__(self):
        return self.coursecode

class States(db.Model):
    __tablename__ = "states"

    stateid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(2))

class Users(db.Model):
    __tablename__ = 'users'

    users_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

class Students(db.Model):
    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(25))

    def __unicode__(self):
        return self.email
