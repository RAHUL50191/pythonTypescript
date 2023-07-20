
import wave
import matplotlib.pyplot as plt
import numpy as np
obj = wave.open("female.wav", 'rb')

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
frames = obj.readframes(-1)

t_audio = n_sample / sample_freq
print(t_audio)
signal_array = np.frombuffer(frames,dtype=np.int16)
times = np.linspace(0, t_audio, num=n_sample)
plt.figure(figsize=(15, 5))
plt.plot(times,signal_array)
plt.title("audio signal")
plt.xlabel("time")
plt.ylabel("signal")

plt.xlim(0, t_audio)
plt.show()