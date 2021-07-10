#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import threading,time,random
from . import configs

class MQTTClient(object):
    """Handles the mqtt connections"""
    def __init__(self, mqttbroker="localhost:1883"):
        super(MQTTClient, self).__init__()
        self.mqttbroker = mqttbroker
        #Connection
        trimed = mqttbroker.split(':')
        self.mqttserver = trimed[0]
        self.mqttport   = int(trimed[1])
        self.mqClient = mqtt.Client(clientName)
        self.mqClient.connect(self.mqttserver, self.mqttport)
        #MQTT Subscriber
        self.mqClient.on_message = self.on_message
        self.mqClient.subscribe(configs.downlinktopic)

        recdata = threading.Thread(
            target=self.receiveDataFromLWan
        )
        recdata.start()

    def receiveDataFromLWan(self):
        self.mqClient.loop_forever()

    def _getRandLetter(self,total):
        letters = ''
        for x in range(total):
            letters += str(chr(random.randrange(97, 97 + 26)))
        return letters

    def on_message(self,client, userdata, msg):
        pass

    def produceOnMQTT(self,topic,message):
        self.mqClient.publish(topic,message)
