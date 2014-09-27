from app import db

class Enrollments(db.Model):

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
