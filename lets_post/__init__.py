'''
    this the the package for the lets_post app. 
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '9d4fd5ad8f924865891f57437162a140'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # this is showing where the login is located
login_manager.login_message_category = 'info' #bootstrap stuff to beautify the message

from lets_post import route