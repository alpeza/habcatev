import habcatev

class SimpleLed(habcatev.device.Device.Device):
    """docstring for MyDevice."""
    def __init__(self):
        super(SimpleLed, self).__init__()
        self.setSubscriptionArr(['#'])

    def on_message(self,client, userdata, msg):
        print(client)
        print(userdata)
        print(msg)
        print('********************++')
    

SimpleLed().run()
