from flask_wtf import Form
from wtforms.fields import TextField, DateField, SubmitField
from wtforms import validators

class ScheduleForm(Form):
    coursecode = TextField
