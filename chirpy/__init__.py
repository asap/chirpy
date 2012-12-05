# -*- coding: utf-8 -*-
"""
Chirpy
======

"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from config import Config


app = Flask(__name__)

# load the default config object. The object is configured to load default or
# load os.environ.get()
app.config.from_object(Config)
Bootstrap(app)

# this try block allows local development settings to be set
try:
    app.config.from_pyfile('local_settings.cfg')
except (RuntimeError, IOError):
    # local settings are not found, we can pass
    pass


#: might lead to circular import; should investigate on doing this better.
from . import views
