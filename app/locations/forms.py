from flask_wtf import Form
from wtforms.fields import TextField, IntegerField
from wtforms import validators

strip_filter = lambda x: x.strip() if x else None


class LocationForm(Form):
    location = TextField('location', filters=[strip_filter])
    facilityname = TextField()
    address = TextField()
    suite = TextField()
    city = TextField()
    state = TextField()
    zipcode = TextField()
    phone = TextField()

    def validate_on_submit(*arg, **kwargs):
        return True



