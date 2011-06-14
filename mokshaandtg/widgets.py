""" My fancy gritter widget """

from moksha.api.widgets.live import LiveWidget

class NotificationWidget(LiveWidget):
    topic = 'foobar'
    onmessage = 'console.log("oh hai")'
    template = "mako:mokshaandtg.templates.nothingspecial"

