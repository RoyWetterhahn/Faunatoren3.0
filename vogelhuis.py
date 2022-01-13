
#main program for the birdhouse
import time
import json
import requests
import pythonConfig as cfg
import PIR
import DHT22
import recorder
import RPi.GPIO as GPIO

def setup():
    GPIO.cleanup()
    global pir_sensor
    global dhtDevice 
    pir_sensor = PIR.setup()
    dhtDevice = DHT22.setup()


def getNewBird():
    with open("/home/pi/BirdNET-Pi/BirdDB.txt", "r") as file:
        for last_line in file:
            pass
    #print(last_line)
    x = last_line.split(";")
    global old_data
    try:
        old_data
    except NameError:
        print("Er is nog geen oude data")
        old_data = "b"
    data = x[3],x[4]
    if old_data != data: 
        print("data to send is ", data)
        old_data = data
        dict_json2 = {
        "deviceId": "A-model-sensor-A",
        "species": str(x[3]),
        "confidence": x[4]
        }
        with open('json2.json', 'w') as f:
            json.dump(dict_json2, f)
        return True
    return False

def eventLoop():
    while True:
        birdData = getNewBird()
        if birdData:
            header = {"Content-Type":"application/json"}
            x = requests.post(cfg.url_id, data=open('json2.json', 'rb'), headers=header)
        PIR_value =  PIR.run(pir_sensor)
        temp, hum = DHT22.run(dhtDevice)
        dict_json1 = {
            "deviceId": str("A2"),
            "modelType": str("A_model"),
            "temperature": temp-20,
            "humidity": hum,
            "movement": int(PIR_value)
        }
        with open('json1.json', 'w') as f:
            json.dump(dict_json1, f)
        time.sleep(1)
        #print("config string = ", cfg.url)
        header = {"Content-Type":"application/json"}
        x = requests.post(cfg.url, data=open('json1.json', 'rb'), headers=header)
        
        
if __name__ == '__main__':
   print("Vogelhuisje wordt gestart")
   setup()
   #start the event loop
   eventLoop()
