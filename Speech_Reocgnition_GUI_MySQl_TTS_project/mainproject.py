import tkinter as tk  #GUI
from sr import sp_recognize
from mysql2 import retrive,retrivecount

frame = tk.Tk()   #GUI frame as "frame"
frame.title("Bhuvan's GUI")   #Title of Frame
frame.geometry('500x500')

SpeakButton = tk.Button(frame,text = "Speak",command =sp_recognize)
SpeakButton.pack()

RetriveButton = tk.Button(frame,text = "Show Records",command =retrive)
RetriveButton.pack()

RowCountButton = tk.Button(frame,text = "Row count",command =retrivecount)
RowCountButton.pack()

frame.mainloop()
