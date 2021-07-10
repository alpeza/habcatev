import paho.mqtt.client as mqtt
import time 
from . import MQTTClient

class Device(MQTTClient.MQTTClient):
    """docstring for Device."""
    def __init__(self,mqttbroker="localhost:1883"):
        super(Device, self).__init__()
        self._subscriptionarr = ['#']

    def setSubscriptionArr(self,subarr):
        self._subscriptionarr = subarr
    
    def run(self):
        # Iniciamos el mqtt
        self.connect()
        self.subscribeto(self.subscriptionarr)
        self._startListeners()

    def on_message(self,client, userdata, msg):
        pass