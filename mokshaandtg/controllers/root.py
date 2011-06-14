# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from mokshaandtg.lib.base import BaseController

from mokshaandtg.controllers.error import ErrorController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the moksha-and-tg application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()

    @expose('mokshaandtg.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('mokshaandtg.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('mokshaandtg.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment=request.environ)

    @expose('mokshaandtg.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)

