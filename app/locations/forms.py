from flask_wtf import Form
from wtforms.fields import TextField, IntegerField
from wtforms import validators


class LocationForm(Form):
    location = TextField('location')
    facilityname = TextField()
    address = TextField()
    suite = TextField()
    city = TextField()
    state = TextField()
    zipcode = TextField()
    phone = TextField()

    def validate_on_submit(*arg, **kwargs):
        return True



