# -*- coding: utf-8 -*-
"""
views
=====


"""

from . import app
from flask import render_template, url_for

chirps = [
    {'name': 'stark', 'chirp':'Winter is Coming'},
    {'name': 'fury', 'chirp':'...'},
]


@app.route('/')
def index():
    return render_template('index.html', chirps=chirps)


@app.route('/add/')
def add():
    return render_template('add.html', chirps=chirps)
