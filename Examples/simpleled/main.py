import habcatev,time

class SimpleLed(habcatev.device.Device.Device):
    """docstring for MyDevice."""
    def __init__(self):
        super(SimpleLed, self).__init__()
        self.setSubscriptionArr(['#'])

    def on_event(self,topic,data):
        print("Topic:" + topic + "  Data: " + data)

    def loop(self):
        print('hola')
        time.sleep(5)

SimpleLed().run()
