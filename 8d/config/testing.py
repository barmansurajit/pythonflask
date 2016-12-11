import os

DEBUG = False
TESTING = True
SECRET_KEY = 'top secret!'
WTF_CSRF_ENABLED = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), '../the_app_test.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True