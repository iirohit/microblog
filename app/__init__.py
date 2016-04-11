from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))
mail = Mail(app)

from .momentjs import momentjs
app.jinja_env.globals['momentjs'] = momentjs

from app import views, models