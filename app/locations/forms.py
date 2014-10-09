from flask_wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField
from wtforms import validators

strip_filter = lambda x: x.strip() if x else None


class LocationForm(Form):
    location = SelectField('location')
    facilityname = TextField('facilityname', filters=[strip_filter])
    address = TextField('address', filters=[strip_filter])
    suite = TextField('suite', filters=[strip_filter])
    city = TextField('city', filters=[strip_filter])
    ###state = SelectField('state', filters=[('1', 'AL'), ('2', 'IL'), ('3', 'CA'), ('4', 'MI')])
    state = SelectField(u'state', coerce=int)
    zipcode = TextField('zipcode', filters=[strip_filter])
    phone = TextField('phone', filters=[strip_filter])

    def validate_on_submit(*arg, **kwargs):
        return True



