from flask_wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms import validators

strip_filter = lambda x: x.strip() if x else None

class UserLoginForm(Form):
    username = TextField('username', [validators.required()], filters=[strip_filter])
    password = PasswordField('password', [validators.required()], filters=[strip_filter])
