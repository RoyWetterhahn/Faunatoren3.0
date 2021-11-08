import os
import time
import requests
import pythonConfig as cfg
import RPi.GPIO as GPIO

def setup():
   GPIO.setmode(GPIO.BOARD)
   print("PIR pin setup")
   GPIO.setup(cfg.PIR_pin, GPIO.IN)
   PIR_value = 0
    
def run():
   if GPIO.input(cfg.PIR_pin):
      PIR_value = 1
      print("Motion detected")
      return PIR_value
   else: 
      PIR_value = 0
      return PIR_value

if __name__ == '__main__':
   print("Dit is de PIR test")
   setup()
   while True: 
      while (run()):
         time.sleep(5)
      time.sleep(1)

