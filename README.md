# Faunatoren3.0
Hier zijn de bestanden en documentatie van de Pi te vinden.<br />

Sensor code uitleg: <br />
De sensor bestanden zijn los van elkaar te draaien zodat deze getest kunnen worden.<br />

PIR.py = code infarood sensor<br />
DHT11.py = temperatuur en humidity sensor<br />
recorder.py = de usb microfoon<br />
pythonConfig.py = staan alle instellingen, zoals hoe de pins zijn aangesloten<br />
vogelhuis.py = het hoofdprogramma roept de functie van verschillende sensoren aan<br />
Bij het opstarten van de Pi wordt middels crontab vogelhuis.py gestart <br />

