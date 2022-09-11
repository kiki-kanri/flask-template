DATABASES = {
    'default': {
        'authentication_source': 'admin',
        'db': '',
        'host': '127.0.0.1',
        'password': '',
        'port': 27017,
        'username': ''
    }
}

DEBUG = True

INSTALL_APPS = [
    'example'
]

# Mail
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_PORT = 587
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USE_TLS = True
MAIL_USE_SSL = False
USE_CREDENTIALS = True
VALIDATE_CERTS = True
# MAIL_DEFAULT_SENDER = ''

SECRET_KEY = ''
