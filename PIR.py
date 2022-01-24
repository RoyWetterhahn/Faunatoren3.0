#Passive infared sensor
import os
import time
import requests
#import pythonConfig as cfg
#import RPi.GPIO as GPIO
import board
import digitalio

def setup():
   pir_sensor = digitalio.DigitalInOut(board.D14)
   pir_sensor.direction = digitalio.Direction.INPUT
   return pir_sensor

# Kijk of de PIR sensor in de afgelopen ~6 sec beweging heeft gezien
# 1 = beweging
# 0 = Geen beweging
def run(pir_sensor):
    if pir_sensor.value:
        return 1
    else: 
        return 0

if __name__ == '__main__':
   print("Dit is de PIR test")
   pir_sensor = setup()
   for i in range(20):
      print(run(pir_sensor))
      time.sleep(3)

