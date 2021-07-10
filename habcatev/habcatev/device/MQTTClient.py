import paho.mqtt.client as mqtt
import threading,time

class MQTTClient(object):
    """Handles the mqtt connections"""
    def __init__(self, brokermqtt="localhost:1883"):
        super(MQTTClient, self).__init__()
        #Connection
        trimed = brokermqtt.split(':')
        self.mqttserver = trimed[0]
        self.mqttport   = int(trimed[1])
        self.deviceid = "habcatdevice-" + str(int(time.time()))
        self.mqClient = mqtt.Client(self.deviceid)
    
    def connect(self):
        self.mqClient.connect(self.mqttserver, self.mqttport)
    
    def _receiveDataFromMQTT(self):
        self.mqClient.loop_forever()
    
    def _startListeners(self):
        recdata = threading.Thread(
            target=self._receiveDataFromMQTT
        )
        recdata.start()
    
    def subscribeto(self,subscriptionsarr):
        self.mqClient.on_message = self.on_message
        for topic in subscriptionsarr:
            self.mqClient.subscribe(topic)


    def send(self,topic,message):
        """ Envia un mensaje a un determinado topic """
        self.mqClient.publish(topic,message)
    
    def on_message(self,client, userdata, msg):
        pass