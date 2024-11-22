# This is a pet project, mimicing the demo from CFG Into to Python

from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Anson's Pet Project")
root.geometry("650x400")
root.config(background = "#0b5428")

header = Label(root, text="Spell Checker")
header.pack()

secondary_header = Label(root, text="Type a word in the field below andd find out!")
secondary_header.pack()

input = StringVar()
text_entry = Entry(root, textvariable=input)
text_entry.pack()

check_btn = Button(root, text="Check!")
check_btn.pack()

root.mainloop()
