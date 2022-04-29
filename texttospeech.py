from cProfile import label
from cgitb import text
from importlib.resources import path
from logging import RootLogger
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from pkg_resources import WorkingSet
import pyttsx3
import os

root =Tk()
root.title("Text to speech")
root.geometry("900x650")
root.resizable(False,False)
root.configure(bg="#F77A64")
engine= pyttsx3.init()


#function for speech

def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='male'):
         engine.setProperty('voice',voices[0].id)  
         engine.say(text)
         engine.runAndWait() 

        else:
         engine.setProperty('voice',voices[1].id)  
         engine.say(text)
         engine.runAndWait() 

    if(text):
        if(speed=="fast"):
            engine.setProperty('rate',250) 
            setvoice()
        elif(speed=='normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
             engine.setProperty('rate', 60)
             setvoice()

#function for downloading the file

def download():
   text = text_area.get(1.0, END)
   gender = gender_combobox.get()
   speed = speed_combobox.get()
   voices = engine.getProperty('voices')

   def setvoice():
        if(gender == 'male'):
         engine.setProperty('voice', voices[0].id)
         path=filedialog.askdirectory()
         os.chdir(path)
         engine.save_to_file(text,'text.mp3')
         engine.runAndWait()

        else:
         engine.setProperty('voice', voices[1].id)
         path = filedialog.askdirectory()
         os.chdir(path)
         engine.save_to_file(text, 'text.mp3')
         engine.runAndWait()

   if(text):
        if(speed == "fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == 'normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


#function for user interface

button_mode=True

def customize():

    global button_mode

    if button_mode:
        button.config(image=off,bg="#26242f",activebackground="#26242f")   
        root.config(bg="#26242f")
        button_mode=False

    else:
        button.config(image=on, bg="#F77A64", activebackground="#F77A64")
        root.config(bg="#F77A64")
        button_mode = True

            
#theme lightmode darkmode
on=PhotoImage(file="light.png")
off = PhotoImage(file="dark.png")

button=Button(root,image=on,bd=0,bg="white",activebackground="white",command= customize)
button.pack(padx=50,pady=120)
         

#icon
image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#top-frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)

Label(Top_frame,text="Text to speech",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

Label(Top_frame,text="By Muhtadin Mushfiq",font="arial 10 bold",bg="white",fg="black").place(x=115,y=60)

#textarea

text_area=Text(root,font="robote 20",bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=270,width=500,height=250)



#voice combobox

Label(root, text="voice", font="arial 15 bold",
      bg='#305065', fg="white").place(x=580, y=260)

gender_combobox=Combobox(root,values=['male','female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=300)
gender_combobox.set('male')


#speed combobox
Label(root, text="speed", font="arial 15 bold",
      bg='#305065', fg="white").place(x=760, y=260)

speed_combobox=Combobox(root,values=['fast','normal','slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=300)
speed_combobox.set('normal')


imageicon=PhotoImage(file="speak.png")
btn=Button(root,text="speak",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=400)

#download button
imageicon2=PhotoImage(file="download.png")
save=Button(root,text="download",compound=LEFT,image=imageicon2,width=150,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=730,y=400)



root.mainloop()
