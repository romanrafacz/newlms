from app import db
from app.enrollments.models import Enrollments
from app.enrollments.forms import EnrollmentForm

from flask import render_template, Blueprint

enrollments_blueprint = Blueprint(
        'enrollments', __name__,
        template_folder = 'templates'
        )

@enrollments_blueprint.route('/enrollments')
def index():
    schedule = db.session.query(Enrollments).group_by(Enrollments.coursecode).order_by(Enrollments.startdate, Enrollments.coursecode).all()
    return render_template('enrollments.html', courses=schedule)

@enrollments_blueprint.route('/enrollmentsbycourse/<int:enrollmentid>/<coursecode>')
def enrollmentsbycourse(enrollmentid, coursecode):
    enrollment = db.session.query(Enrollments).filter_by(id=enrollmentid).first()
    classroster = db.session.query(Enrollments.studentname, Enrollments.studentemail).filter_by(coursecode=coursecode).all()
    return render_template("enrollmentsbycourse.html", course=enrollment, roster=classroster)

@enrollments_blueprint.route('/addenrollment', methods=['POST', 'GET'])
def addenrollment():
    enrollmentform = EnrollmentForm()
    return render_template("addenrollment.html", enrollmentform=enrollmentform)

