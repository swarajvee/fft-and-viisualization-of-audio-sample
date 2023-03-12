import numpy as np 
import matplotlib.pyplot as plt 
import librosa
from librosa import display

audio, sr = librosa.load('/Users/swarajv/Education/python programs/sem 8/fourier transform /source/bass guitar.wav', mono=True)
plt.style.use('ggplot')
librosa.display.waveshow(audio,sr)
plt.title("Visualization of audio sample")
plt.xlabel("Time(in seconds)")
plt.ylabel("Amplitude")
plt.show()