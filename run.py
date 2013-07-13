""" Web application entry point

A specific config branch can be forced by a supplied parameter, e.g.
run.py development
run.py production

"""
from app import app

app.run()