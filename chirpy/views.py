# -*- coding: utf-8 -*-
"""
views
=====


"""

from . import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')
