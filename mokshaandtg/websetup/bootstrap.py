# -*- coding: utf-8 -*-
"""Setup the moksha-and-tg application"""

import logging
from tg import config
from mokshaandtg import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup mokshaandtg here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
