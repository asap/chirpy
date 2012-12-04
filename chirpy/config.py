# -*- coding: utf-8 -*-
"""
   Configuration Settings.
   =======================

   Global configuration settings.
"""


from os import environ


class Config(object):
    """Adding a setting here makes it global.
    """

    #: Always False
    DEBUG = False

    #: Testing setting
    TESTING = environ.get('TESTING', False)

    #: csrf setting.
    CSRF_ENABLED = False
