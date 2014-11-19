from flask import render_template, Blueprint
from app import db
from app.models import Course

courses_blueprint = Blueprint(
        'courses', __name__,
        template_folder='templates'
        )

@courses_blueprint.route('/courses')
def courses():
    courses = db.session.query(Course).all()
    return render_template('courses.html', courses=courses)
