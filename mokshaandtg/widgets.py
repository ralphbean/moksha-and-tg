""" My fancy gritter widget """

from moksha.api.widgets.live import TW2LiveWidget
from tw2.jqplugins.gritter import gritter_resources

lulz = 'http://a1.twimg.com/profile_images/1341989664/somehwat-mad-completely-mad-u-mad-MADAD.jpg'

class NotificationWidget(TW2LiveWidget):
    topic = 'foobar'
    onmessage = """
            $.gritter.add({
                title: 'This is an AMQP message via Orbited!',
                text: json['message'],
                image: '%s',
                sticky: false,
                time: '',
            })
    """ % lulz
    resources = TW2LiveWidget.resources + gritter_resources
    template = "mako:mokshaandtg.templates.nothingspecial"

