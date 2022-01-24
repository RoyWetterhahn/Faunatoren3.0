#hoofdprogramma voor het vogelhuis
import time
import json
import requests
import pythonConfig as cfg
import PIR
import DHT22
import recorder
import RPi.GPIO as GPIO

#de setup van de verschillende sensoren
def setup():
    GPIO.cleanup()
    global pir_sensor
    global dhtDevice 
    pir_sensor = PIR.setup()
    dhtDevice = DHT22.setup()

#Kijk of er een nieuwe vogel is en zo ja, zet deze in json2.json
def getNewBird():
    #Lees birdnet DataBase uit
    with open("/home/pi/BirdNET-Pi/BirdDB.txt", "r") as file:
        for last_line in file:
            pass
    x = last_line.split(";")
    #Check of vogel data is verandert
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
        strBird = str(x[3])
        underscoreStr = strBird.replace(" ", "_")
        print(underscoreStr)
        dict_json2 = {
        "deviceId": cfg.device_id,
        "species": underscoreStr,
        "confidence": x[4]
        }
        #update json2 met de nieuwe data
        with open('/home/pi/Faunatoren/json2.json', 'w') as f:
            json.dump(dict_json2, f)
        return True
    return False

#eventloop van het programma, hierin wordt om de zoveel tijd alle sensor waarnemingen geupdate
def eventLoop():
    while True:
        birdData = getNewBird()
        #Als er nieuwe vogelData is verstuur deze
        if birdData: 
            print("json2 wordt gestuurd")
            header = {"Content-Type":"application/json"}
            x = requests.post(cfg.url_id, data=open('/home/pi/Faunatoren/json2.json', 'rb'), headers=header)
        PIR_value =  PIR.run(pir_sensor)
        temp, hum = DHT22.run(dhtDevice)
        dict_json1 = {
            "deviceId": cfg.device_id,
            "modelType": str("A_model"),
            "temperature": temp,
            "humidity": hum,
            "movement": int(PIR_value)
        }
        #updatejson1 met nieuwe data
        with open('/home/pi/Faunatoren/json1.json', 'w') as f:
            json.dump(dict_json1, f)
        time.sleep(1)
        header = {"Content-Type":"application/json"}
        x = requests.post(cfg.url, data=open('/home/pi/Faunatoren/json1.json', 'rb'), headers=header)
        
        
if __name__ == '__main__':
   print("Vogelhuisje wordt gestart")
   setup()
   #start the event loop
   eventLoop()
