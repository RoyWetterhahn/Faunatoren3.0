import time
import board
import adafruit_dht
import requests
import pythonConfig as cfg

def setup():
   print("DHT pin setup")
   dhtDevice = adafruit_dht.DHT11(cfg.DHT_pin)
   return (dhtDevice)

def run(dhtDevice):
     temperature_c = dhtDevice.temperature
     humidity = dhtDevice.humidity
     return (temperature_c, humidity)

if __name__ == '__main__':
   print("Dit is de DHT test")
   dhtDevice = setup()
   while True: 
     temperature_c, humidity = run(dhtDevice)
     print("Temp: {:.1f} C    Humidity: {}% " .format(temperature_c, humidity))      
     time.sleep(2)
s