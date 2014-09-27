from app import db
from app.enrollments.models import Enrollments

from flask import render_template, Blueprint

enrollments_blueprint = Blueprint(
        'enrollments', __name__,
        template_folder = 'templates'
        )

@enrollments_blueprint.route('/enrollments')
def enrollments():
    courseschedule = db.session.query(Enrollments).all()
    return render_template('index.html', courseschedule=courseschedule)

