# -*- coding: utf-8 -*-

"""The base Controller API."""

from tg import TGController, tmpl_context
from tg.render import render
from pylons.i18n import _, ungettext, N_

import moksha.lib.base
import mokshaandtg.widgets

__all__ = ['BaseController']


class BaseController(TGController):
    """
    Base class for the controllers in the application.

    Your web application should have one of these. The root of
    your application is used to compute URLs used by your app.

    """

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # TGController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        #tmpl_context.notif = mokshaandtg.widgets.NotificationWidget(id='foo').display()
        tmpl_context.notif = moksha.utils.get_widget('garbage').display()
        # I want to use my own lib/base
        tmpl_context.globs = moksha.lib.base.global_resources()

        return TGController.__call__(self, environ, start_response)
