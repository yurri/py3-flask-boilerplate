#!python
""" Gets console prompt to run app and system functions
e.g. to initialise a database or to see debug print

"""

try:
    import readline                 # unix
except ImportError:
    import pyreadline as readline   # windows

import os
from pprint import pprint
from flask import *

from app import *
import config

os.environ['PYTHONINSPECT'] = 'True'