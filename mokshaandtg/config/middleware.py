# -*- coding: utf-8 -*-
"""WSGI middleware initialization for the moksha-and-tg application."""

from mokshaandtg.config.app_cfg import base_config
from mokshaandtg.config.environment import load_environment


__all__ = ['make_app']

# Use base_config to setup the necessary PasteDeploy application factory. 
# make_base_app will wrap the TG2 app with all the middleware it needs. 
make_base_app = base_config.setup_tg_wsgi_app(load_environment)

from moksha.middleware import make_moksha_middleware

def make_app(global_conf, full_stack=True, **app_conf):
    """
    Set moksha-and-tg up with the settings found in the PasteDeploy configuration
    file used.
    
    :param global_conf: The global settings for moksha-and-tg (those
        defined under the ``[DEFAULT]`` section).
    :type global_conf: dict
    :param full_stack: Should the whole TG2 stack be set up?
    :type full_stack: str or bool
    :return: The moksha-and-tg application with all the relevant middleware
        loaded.
    
    This is the PasteDeploy factory for the moksha-and-tg application.
    
    ``app_conf`` contains all the application-specific settings (those defined
    under ``[app:main]``.
    
   
    """
    app = make_base_app(global_conf, full_stack=True,
                        wrap_app=make_moksha_middleware,
                        **app_conf)
    
    # Wrap your base TurboGears 2 application with custom middleware here
    
    return app
