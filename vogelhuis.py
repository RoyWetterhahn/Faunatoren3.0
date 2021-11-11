import os
import time
import requests
import pythonConfig as cfg
import PIR
import DHT11
import recorder
import RPi.GPIO as GPIO
from threading import Thread

def setup():
    GPIO.cleanup()
    PIR.setup()
    global dhtDevice 
    dhtDevice = DHT11.setup()
    
def sendData(id, value):
    print("sending data ", id)
    myobj = {'id': id, 'value': value}
    # send data to dashboard
    x = requests.post(cfg.url, json = myobj)

def eventLoop():
    while True:
        #send data to database
        print("PIR value = ", PIR.run())
        temp, hum = DHT11.run(dhtDevice)
        print("Temp Humidity = ", temp, hum)
        recorder.run()
        sendData("movementData", PIR.run())
        print("temperature == ", temp)
        sendData("temperatureData", temp)
        sendData("humidityData", hum)
        time.sleep(1)

if __name__ == '__main__':
   print("Vogelhuisje wordt gestart")
   setup()
   #start the event loop
   eventLoop()
