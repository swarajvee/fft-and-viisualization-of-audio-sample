from tkinter import *
from tkinter import filedialog

def OpenFile():
    filepath=filedialog.askopenfilename(title='open file',\
        filetypes=(('wav files','*.wav'),('m4a files','*.m4a'),\
            ('mp3 files','*mp3'),('ogg files','*.ogg'),\
                ('flac files','*.flac'),('aiff files','*.aiff'),\
                    ('au files','*.au'),\
                    ('all files','*.*')))

    print(filepath)
    file = open(filepath,'r')
    file.close()

window = Tk()
button=Button(text='select audio sample',command= OpenFile)
button.pack()
window.mainloop()
