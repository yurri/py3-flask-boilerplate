from flask import Flask, render_template

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from os import path
import config

"""Initialise database"""
if config.get('db', 'type') == 'sqlite':
    connection_string = 'sqlite:////' + path.join(config.DATA_PATH, config.get('db', 'file'))
else:
    raise KeyError("Unrecognised database type in configuration file")

# so we can inherit our model classes from Base
Base = declarative_base()
# initialise db connection
db_engine = create_engine(connection_string)
# initialise db session to handle threads for us
scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))

def init_db():
    """Performs db initialisation creating tables as models define"""
    import models
    Base.metadata.create_all(bind=db_engine)

"""Initialise app"""
app = Flask(__name__)
app.config.update(config.get('flask'))

"""Application routes (actions)"""
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def home():
  return render_template('home.html')

# adding a module
#from app.users.views import mod as usersModule
# app.register_blueprint(usersModule)
