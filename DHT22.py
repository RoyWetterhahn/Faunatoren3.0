#DHT11 Temperature, humidity senor
import time
import board
import Adafruit_DHT
#import adafruit_dht
import requests
import pythonConfig as cfg


def setup():
   print("DHT pin setup")
   dhtDevice = Adafruit_DHT.DHT22
   return (dhtDevice)

def run(dhtDevice):
     temperature_c, humidity = Adafruit_DHT.read_retry(dhtDevice, cfg.DHT_pin)
     return (temperature_c, humidity)

if __name__ == '__main__':
   print("Dit is de DHT test")
   dhtDevice = setup()
   while True: 
     temperature_c, humidity = run(dhtDevice)
     print("Temp: {:.1f} C    Humidity: {}% " .format(temperature_c-48, humidity))
     time.sleep(2)
