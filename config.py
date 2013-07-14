""" Reads configuration from file and also adds some run-time constants

When the app is initialised, Flask-specific config can be loaded as app.config.update(config.get('flask'))

"""
import sys
from os import path

APP_PATH = path.abspath(path.dirname(__file__))     # application root path
DATA_PATH = path.join(APP_PATH, 'app', 'data')      # data path e.g. for SQLite dbs

sys.path.insert(0, path.join(APP_PATH, 'app'))    # add models to include path

import json
with open(path.join(APP_PATH, 'app', 'config', 'config.json')) as f:
    _config_all = json.loads(f.read())   # whole config json

if len(sys.argv) > 1:
    _mode = sys.argv[1]             # config branch forced in command line
else:
    _mode = _config_all['mode']     # action config branch read from config itself

config = _config_all['modes'][_mode]   # config branch for requested mode

def get(*arg, default = None):
    """ Reads configuration value safely without exceptions on absent keys
    get(['flask', 'DEBUG'], False) will return config['flask']['DEBUG'] or False if it doesn't exist
    get('flask') also supported as well as get(['flask'])

    """

    pointer = config
    for key in arg:
        try:
            pointer = pointer[key]
        except KeyError:
            return default

    return pointer
