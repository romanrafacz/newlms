DEBUG=True

SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost/jmdb'

SECRET_KEY = "this is a secret"

WTF_CSRF_SECRET_KEY = "to jest secret"


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TSL = True
MAIL_USE_SSL = False 
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
SMTP_SECURE = True
VARIFY = False
