from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3

def caliberateBgNoise():
    with sr.Microphone() as source2:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source2, duration=3)
    
def caliberate():
    l1 = Label(text="Wait a minute, caliberating...", font="georgia 15",background="#4a4a4a",fg="white")
#    l1.place(x=285,y=323)
    l1.place(x=215,y=323)
    root.update()
    caliberateBgNoise()
    l1.config(text="")
    l2 = Label(text="Yup done!", font="georgia 15",background="#4a4a4a",fg="white")
#    l2.place(x=285,y=323)
    l2.place(x=215,y=323)
    
    
#global labelSpeech
#labelSpeech = Label(text="",font="georgia 15",background="#4a4a4a",fg="white", wraplength="500")
#labelSpeech.place(x=50,y=415)
    
def recognise():
    Label(root,text="",font="15",background="black",width=1000,height=1000).place(x=0,y=415)
    with sr.Microphone() as source2:
        r = sr.Recognizer()
        audio2 = r.listen(source2)
        myspeech = r.recognize_google(audio2)
               
    labelRecog = Label(text="Did you say ->", font="georgia 15",background="#4a4a4a",fg="white")
#    labelRecog.place(x=250,y=373)
    labelRecog.place(x=180,y=373)

    labelSpeech = Label(text=myspeech,font="georgia 15",background="black",fg="white", wraplength="500")
#   labelSpeech.config(text=myspeech)
    labelSpeech.place(x=50,y=420)
    root.update()
    
    engine = pyttsx3.init()
    engine.say(myspeech)
    engine.runAndWait()
    

root = Tk()
root.geometry("600x700+400+80")
root.resizable(False, False)
root.title("Speech Recognition v2.0")
root.config(background='#4a4a4a')
    
#icon
#imageIcon=PhotoImage(file="AAA.png")
#root.iconphoto(False,imageIcon)
    
#logo
imageLogo=PhotoImage(file="AAA.png")
myimg=Label(image=imageLogo,background="#4a4a4a")
myimg.pack(padx=10,pady=25)

#Field Title label
Label(text="Speech Recognition", font="georgia 30",background="#4a4a4a",fg="white").pack()

#Buttons
calib=Button(root,font="georgia 15",text="Caliberate Noise",bg="#111111",fg="white",border=0,command=caliberate)
#caliberate.place(x=120,y=320)
calib.place(x=50,y=320)
root.update()

recognz=Button(root,font="georgia 15",text="Recognise...",bg="#111111",fg="white",border=0,command=recognise)
#recognz.place(x=120,y=370)
recognz.place(x=50,y=370)
root.update()

Label(root,text="",font="15",background="black",width=1000,height=1000).place(x=0,y=415)

root.mainloop()
