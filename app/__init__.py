from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('devconfig')

####################
#db object

db = SQLAlchemy(app)


####################
#Import and Register Blueprints
####################

from app.home.views import home_blueprint
from app.courses.views import courses_blueprint
from app.locations.views import locations_blueprint
from app.schedule.views import schedule_blueprint
from app.students.views import students_blueprint
from app.enrollments.views import enrollments_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(courses_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(students_blueprint)
app.register_blueprint(enrollments_blueprint)
