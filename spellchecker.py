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

text_entry = Entry(root)
text_entry.pack()

def spell_check():
    input = text_entry.get()
    suggested_spelling = str(TextBlob(input).correct())
    
    result_text = ""
    if input == suggested_spelling:
        result_text = f"Congrats! You spell {input} correctly!"
    else:
        result_text = f"Could you mean {suggested_spelling} instead?"
    result_display.config(text=result_text)

check_btn = Button(root, text="Check!", command=spell_check)
check_btn.pack()

result_display = Label(root)
result_display.pack()

root.mainloop()
