from flask import Flask, render_template
from os import path

import config
import db

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')

@app.after_request
def shutdown_session(response):
    """Clear db session for correct multi-threading"""
    db.session.remove()
    return response

# adding a module
#from app.users.views import mod as usersModule
# app.register_blueprint(usersModule)
