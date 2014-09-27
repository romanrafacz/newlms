#Instert models here
from __future__ import print_function

from app import db


class Course(db.Model):
    __tablename__ = "course"

    courseid = db.Column(db.Integer, primary_key=True)
    coursecode = db.Column(db.String(6))
    coursename = db.Column(db.String(120))
    price = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    schedule = db.relationship("Schedule", lazy="joined", backref="course")

    def __unicode__(self):
        return self.coursecode


class Location(db.Model):
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True)
    facilityname = db.Column(db.String(120))
    facilityname2 = db.Column(db.String(150))
    address = db.Column(db.String(120))
    address2 = db.Column(db.String(120))
    city_state = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.Integer)
    phone = db.Column(db.String(120))
    scheduleid = db.relationship("Schedule", lazy="joined", backref="location")

    def __unicode__(self):
        return self.facilityname

    def __repr__(self):
        return self.facilityname

class Student(db.Model):
    __tablename__ = "student"

    studentid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(122))
    lastname = db.Column(db.String(122))
    email = db.Column(db.String(122))
    courseid = db.relationship("StudentCourse", backref="student")


    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "<Student {0.lastname}, {0.firstname}>".format(self)

    def __repr__(self):
        return "<Student (%s)>" % self.lastname

class StudentCourse(db.Model):
    __tablename__ = "studentcourse"

    studentclassid = db.Column(db.Integer, primary_key=True)
    studentid = db.Column(db.Integer, db.ForeignKey('student.studentid'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseid.id'))

    def __repr__(self):
        return "<CourseID: %s" % (self.courseid)

class Instructor(db.Model):
    __tablename__ = "instructor"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(122))
    lastname = db.Column(db.String(122))
    email = db.Column(db.String(122))
    phone = db.Column(db.String(122))
    schedule = db.relationship("Schedule", lazy="joined", backref="instructor")

    def __unicode__(self):
        return self.lastname
    
class Schedule(db.Model):
    __tablename__ = "schedule"

    scheduleid = db.Column(db.Integer, primary_key=True)
    locationid = db.Column(db.Integer, db.ForeignKey('location.id'))
    coursecode = db.Column(db.String(6), db.ForeignKey('course.coursecode'))
    startdate = db.Column(db.Date())
    instructorid = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    courseid = db.relationship('Courseid', backref="schedule")

    def __unicode__(self):
        return self.coursecode

class Courseid(db.Model):
    __tablename__ = "courseid"

    id = db.Column(db.Integer, primary_key=True)
    #studentcourseid = db.relationship("StudentCourse", backref="course")
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    company = db.Column(db.String(25))
    enroll_date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    enroll_date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    scheduleid = db.Column(db.Integer, db.ForeignKey('schedule.scheduleid'))
    
    def __repr__(self):
        return "<Coruseid %s" % (self.studentcourseid)

class Contact(db.Model):
    __tablename__ = "contact"
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    request = db.Column(db.Text)
    
#######################
##testing purposes
#######################

class Parent(db.Model):
    __tablename__ = "parent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    children = db.relationship("Child", backref="parent")

    def __repr__(self):
        return "%r" % (self.name)

class Child(db.Model):
    __tablename__ = "child"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    parentid = db.Column(db.Integer, db.ForeignKey('parent.id'))

    def __repr__(self):
        return "<Childe: %r>" % (self.name)


   

