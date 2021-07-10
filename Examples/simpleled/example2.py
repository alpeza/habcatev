import habcatev,time
import random 

class SimpleExample(habcatev.device.Device.Device):
    def __init__(self):
        super(SimpleExample, self).__init__()
        # El dispositivo se subscribe a los topis especificados en la 
        # configuracion
        self.setSubscriptionArr(self.config['ejemplo2']['subscribe'])
        self.deviceDescription = 'Ejemplo simple en el que se produce y consume'

    def on_event(self,topic,data):
        # Lanzamos este codigo cuando se produce un evento
        self.log.logger.info("Ha llegado: Topic:" + topic + "  Data: " + data)

    def loop(self):
        # Suponemos que leemos el valor de un sensor y lo escribimos 
        # en un topic
        self.log.logger.info('Enviando un mensaje a mqtt ...')
        self.send(self.config['ejemplo2']['publish'], random.uniform(10.5, 75.5))
        time.sleep(5)

SimpleExample()
