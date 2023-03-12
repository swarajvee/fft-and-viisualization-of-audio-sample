import numpy as np
import matplotlib.pyplot as plt 
import librosa 

audio, sr = librosa.load("/Users/swarajv/Education/python programs/sem 8/fourier transform /source/bass guitar.wav")

def FFT(audio,sr):
    n=len(audio)
    fft=np.fft.fft(audio)
    x = np.linspace(1,sr/2,n//2 + 1)
    fig,ax =plt.subplots() 
    ax.plot(x,2.0/n*np.abs(fft[:n//2 + 1]))
    plt.grid() 
    plt.xlabel("Frequency -->") 
    plt.ylabel("Magnitude")
    return plt.show()

FFT(audio,sr)