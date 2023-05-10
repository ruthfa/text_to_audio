import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from gtts import gTTS

my_w = tk.Tk()
my_w.geometry("400x300")
my_w.title('pdf to audiobook')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload a pdf file',width=30,font=my_font1)
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', width=20,command = lambda:upload_file())
b1.grid(row=2,column=1)
b2 = tk.Button(my_w, text= "Play", width=20, command = lambda:play_file())
b2.grid(row=3, column=1)

def upload_file():
    f_types = [('pdf', '*.pdf*')]
    file = filedialog.askopenfilename(filetypes=f_types)
    reader = PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()
    with open("pdf/document.txt", "w") as my_file:
        my_file.write(text)

    #return my_w.destroy()

def play_file():
    file = open("pdf/document.txt")
    file = file.read()
    speech = gTTS(text= str(file), lang='en')
    speech.save("pdf_voice.mp3")
    os.system("start pdf_voice.mp3")


my_w.mainloop()



