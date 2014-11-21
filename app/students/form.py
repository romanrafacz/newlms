from flask_wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField

strip_filter = lambda x: x.strip() if x else None

class StudentForm(Form):
    first_name = TextField('fname', filters=[strip_filter])
    last_name = TextField('lname', filters=[strip_filter])
    email = TextField('email', filters=[strip_filter])
    phone = TextField('phone', filters=[strip_filter])
