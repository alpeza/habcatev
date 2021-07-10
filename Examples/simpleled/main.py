import habcatev

class SimpleLed(habcatev.device.Device.Device):
    """docstring for MyDevice."""
    def __init__(self):
        super(SimpleLed, self).__init__()
        print('Hola')

    def onInput(self):
        print('holi')

    def loop(self):
        print('Hola')
    
    def run(self):
        print('running ...')


SimpleLed().run()
