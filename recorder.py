import pyaudio
import wave
import os
import pythonConfig as cfg


def run():
    audio = pyaudio.PyAudio() # create pyaudio instantiation
    # create pyaudio stream
    stream = audio.open(format = cfg.form_1,rate = cfg.samp_rate,channels = cfg.chans, \
                        input_device_index = cfg.dev_index,input = True, \
                        frames_per_buffer=cfg.chunk)
    print("recording")
    frames = []
    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((cfg.samp_rate/cfg.chunk)*cfg.record_secs)):
        data = stream.read(cfg.chunk)
        frames.append(data)
    print("finished recording")
    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()
    # save the audio frames as .wav file
    wavefile = wave.open(os.path.join(cfg.audioDir, cfg.wav_output_filename),'wb')
    wavefile.setnchannels(cfg.chans)
    wavefile.setsampwidth(audio.get_sample_size(cfg.form_1))
    wavefile.setframerate(cfg.samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close() 

if __name__ == '__main__':
    run()

def listDevices(): 
    p = pyaudio.PyAudio()
    print("device count = ", p.get_device_count())
    for ii in range(p.get_device_count()):
        print(p.get_device_info_by_index(ii).get('name'))

