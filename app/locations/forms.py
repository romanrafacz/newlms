from flask_wtf import Form
from wtforms.field import TextField, IntegerField

class LocationForm(Form):
    faclityname = TextField()
    faclityname2 = TextField()
    address = TextField()
    address2 = TextField()
    city = TextField()
    state = TextField()
    zipcode = TextField()
    phone = TextField()



