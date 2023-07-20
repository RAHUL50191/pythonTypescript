import wave
import pyaudio

FRAME_PER_BUFFER=4000
FORMAT=pyaudio.paInt16
CHANNEL=1
RATE=16000

p=pyaudio.PyAudio()
stream =p.open(
    format=FORMAT,
    frames_per_buffer=FRAME_PER_BUFFER,
    channels=CHANNEL,
    rate=RATE,
    input=True
)
seconds=15
frames=[]
print("start recording")
for i in range(0, int (RATE/FRAME_PER_BUFFER*seconds)): 
    data =stream.read(FRAME_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

Obj = wave.open("output.wav", "wb")
Obj.setnchannels (CHANNEL)
Obj.setsampwidth (p.get_sample_size (FORMAT))
Obj.setframerate(RATE)
Obj.writeframes (b"".join(frames)) 
Obj.close()
