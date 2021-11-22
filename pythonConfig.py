#config file here are al the global settings
import board
import pyaudio

#Ip adres dashboard
url = 'http://172.31.99.222/api/widget'
#pin infarood sensor
PIR_pin = 8
PIR_value = 0
#DHT sensor
DHT_pin = board.D4
#Microphone settings
form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
audioDir = '/home/pi/Faunatoren2/github/audioFrag'
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 4 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'example2.wav' # name of .wav file

