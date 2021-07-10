import habcatev,time
import random,json

class Controller(habcatev.device.Device.Device):
    def __init__(self):
        super(Controller, self).__init__()

    def init(self):
        self.setSubscriptionArr(self.config['controller']['subscribe'])
        
    def on_event(self,topic,data):
        self.log.logger.info("Ha llegado: Topic:" + topic + "  Data: " + data)
        datatosend = {
            "datasensor1": None,
            "datasensor2": None,
        }
        print(topic.split('/')[1])
        datatosend[topic.split('/')[1]] = str(data)
        self.send(self.config['controller']['publish'], json.dumps(datatosend))


Controller()
