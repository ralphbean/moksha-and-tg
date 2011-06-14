
from moksha.api.hub.producer import PollingProducer
from datetime import timedelta

class GarbageProducer(PollingProducer):
    frequency = timedelta(seconds=2)
    jsonify = True

    def poll(self):
        self.send_message('foobar', {'message': 'oh hai there'})

