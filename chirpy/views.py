# -*- coding: utf-8 -*-
"""
views
=====


"""

from . import app
from flask import render_template

chirps = [
    # {'name': 'stark', 'chirp':'Winter is Coming'},
    # {'name': 'fury', 'chirp':'...'},
]


@app.route('/')
def index():
    return render_template('index.html', chirps=chirps)
