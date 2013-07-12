""" Reads configuration from file and also adds some run-time constants

When the app is initialised, Flask config can be loaded as: app.config.from_object(config.get('flask'))

"""
import os
APP_PATH = os.path.abspath(os.path.dirname(__file__))    # application root path

import json
with open('app/config/config.json') as f:
    _config_all = json.loads(f.read())   # whole config json

config = _config_all['modes'][_config_all['mode']]   # config branch for requested mode

def get(path, default = None):
    """ Reads configuration value safely without exceptions on absent keys
    get(['flask', 'DEBUG'], False) will return config['flask']['DEBUG'] or False if it doesn't exist
    get('flask') also supported as well as get(['flask'])
    """

    if isinstance(path, str):
        path = [path]

    pointer = config
    for key in path:
        try:
            pointer = pointer[key]
        except KeyError:
            return default

    return pointer
