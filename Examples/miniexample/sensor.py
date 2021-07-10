import habcatev,time
import random 

class Sensor(habcatev.device.Device.Device):
    def __init__(self):
        super(Sensor, self).__init__()

    def loop(self):
        self.log.logger.info('Enviando un mensaje a mqtt ...')
        self.send(self.config['sensor']['publish'], random.uniform(10.5, 75.5))
        time.sleep(self.config['sensor']['sleep'])

Sensor()
