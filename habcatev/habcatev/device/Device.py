import paho.mqtt.client as mqtt
import time 
from . import MQTTClient

class Device(MQTTClient.MQTTClient):
    """docstring for Device."""
    def __init__(self,mqttbroker="localhost:1883", id=""):
        super(Device, self).__init__()
        print('Hello')
        self.deviceid = "habcatdevice-" + id + "-" + str(int(time.time()))

    def on_message(self,client, userdata, msg):
        pass