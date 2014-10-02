from flask_wtf import Form
from wtforms.fields import TextField, SubmitField, IntegerField, TextField, TextAreaField
from wtforms import validators

strip_filter = lambda x: x.strip() if x else None

class ContactForm(Form):
    firstname = TextField('firstname', filters=[strip_filter])
    lastname = TextField('lastname', filters=[strip_filter])
    email = TextField('email', filters=[strip_filter])
    comments = TextAreaField('comments', filters=[strip_filter])
