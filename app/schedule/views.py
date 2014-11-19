from flask import render_template, Blueprint
from app import db
from app.models import Enrollments

schedule_blueprint = Blueprint(
        'schedule', __name__,
        template_folder = 'templates'
        )

@schedule_blueprint.route('/schedule')
def schedule():
    schedule = db.session.query(Enrollments).all()
    return render_template("schedule.html", schedule=schedule)
