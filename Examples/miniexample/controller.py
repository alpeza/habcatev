import habcatev,time
import random,json
from datetime import datetime

class Controller(habcatev.device.Device.Device):
    def __init__(self):
        super(Controller, self).__init__()

    def init(self):
        self.datatosend = {
            "time": None,
            "datasensor1": None,
            "datasensor2": None,
        }
        self.setSubscriptionArr(self.config['controller']['subscribe'])

    def on_event(self,topic,data):
        self.log.logger.info("Ha llegado: Topic:" + topic + "  Data: " + data)
        print(topic.split('/')[1])
        self.datatosend[topic.split('/')[1]] = str(data)
        self.datatosend['time'] = str(datetime.now())
        self.send(self.config['controller']['publish'], json.dumps(self.datatosend))

Controller()
