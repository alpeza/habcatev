import habcatev

class SimpleLed(habcatev.device.Device.Device):
    """docstring for MyDevice."""
    def __init__(self):
        super(SimpleLed, self).__init__()
        self.setSubscriptionArr(['#'])

    def on_event(topic,data):
        print("Topic:" + topic + "  Data: " + data)

    


SimpleLed().run()
