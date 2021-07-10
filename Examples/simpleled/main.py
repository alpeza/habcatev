import habcatev,time
import random 

class SimpleExample(habcatev.device.Device.Device):
    """docstring for MyDevice."""
    def __init__(self):
        super(SimpleExample, self).__init__()
        self.setSubscriptionArr(['#'])

    def on_event(self,topic,data):
        print("Topic:" + topic + "  Data: " + data)

    def loop(self):
        self.send('mitopico1', random.uniform(10.5, 75.5))
        time.sleep(5)

SimpleExample().run()
