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
   #GPIO.cleanup()
   #GPIO.setmode(GPIO.BOARD)
   #print("PIR pin setup")
   #GPIO.setup(8, GPIO.IN)
   #PIR_value = 0
   #print("PIR value = ", GPIO.input(8))

def run(pir_sensor):
    #print("run")
    if pir_sensor.value:
        #print("motion detected")
        return 1
    else: 
        #print("no motion detected")
        return 0
#   if GPIO.input(cfg.PIR_pin):
#      PIR_value = 1
#      print("Motion detected")
#      return PIR_value
#   else: 
#      PIR_value = 0
#      print("no motion Detected")
#      return PIR_value

if __name__ == '__main__':
   print("Dit is de PIR test")
   pir_sensor = setup()
   for i in range(20):
      run(pir_sensor)
      time.sleep(3)

