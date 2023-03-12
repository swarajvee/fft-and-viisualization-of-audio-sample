import numpy as np
import matplotlib.pyplot as plt 
import librosa 
from librosa import display
from tkinter import *
from tkinter import filedialog

#opening dialoguebox
filepath=""
def OpenFile():
    global filepath
    filepath=filedialog.askopenfilename(title='open file',\
        filetypes=(('wav files','*.wav'),('m4a files','*.m4a'),\
            ('mp3 files','*.mp3'),('ogg files','*.ogg'),\
                ('flac files','*.flac'),('aiff files','*.aiff'),\
                    ('au files','*.au'),\
                    ('all files','*.*')))
    window.destroy()
    #print(filepath)
    #file = open(filepath,'r')
    #file.close()

window = Tk()
button=Button(text='select audio sample',command= OpenFile)
button.pack()
window.mainloop()

#making the FFT from the filepath
audio, sr = librosa.load(filepath)

n=len(audio)
fft=np.fft.fft(audio)
x = np.linspace(1,sr/2,n//2 + 1)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1,\
    figsize=(13,9),facecolor='#AFEEEE',\
gridspec_kw={'height_ratios': [1, 2]})

#visualization
librosa.display.waveshow(audio,sr,ax=ax1,color='#20B2AA')
ax1.set_title("Visualization of Audio Sample",fontsize=15,\
    fontfamily="monospace", fontweight='light')
ax1.set_xlabel("Time(in seconds)",fontsize=7)
ax1.set_ylabel("Amplitude")

#fft
ax2.plot(x,2.0/n*np.abs(fft[:n//2 + 1]),color='#20B2AA')
ax2.set_title("FFT of the Audio Signal",fontsize=15,\
    fontfamily="monospace", fontweight='light')
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")  

ax1.grid(True)
ax2.grid(True)

plt.show()