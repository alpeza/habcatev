import habcatev

class SimpleLed(habcatev.device.Device.Device):
    """docstring for MyDevice."""
    def __init__(self):
        super(SimpleLed, self).__init__()
        print('Hola')

    def on_message(self,client, userdata, msg):
        print(client)
        print(userdata)
        print(msg)
        print('********************++')

    def loop(self):
        print('Hola')
    
    def run(self):
        print('running ...')


SimpleLed().run()
