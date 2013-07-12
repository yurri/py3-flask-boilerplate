#!python
""" Gets console prompt to run app and system functions
e.g. to initialise a database or to see debug print

"""

import os
try:
    import readline                 # unix
except ImportError:
    import pyreadline as readline   # windows

from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'