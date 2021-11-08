import os
import time
import requests
import pythonConfig as cfg
import PIR
import RPi.GPIO as GPIO
from threading import Thread

def setup():
    PIR.setup()
    Thread.start(PIR.run())

    
def eventLoop():
    while True:
        #send data to database
        print("PIR value = ", PIR_value)
        myobj = {'id': 'movementData', 'value': PIR.run()}
        # send data to dashboard
        x = requests.post(cfg.url, json = myobj)

if __name__ == '__main__':
   print("Vogelhuisje wordt gestart")
   setup()
   #start the event loop
   eventLoop()
