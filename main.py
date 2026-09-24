import random
import time
from tkinter import *
from sentence import SENTENCES

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

window.columnconfigure(1, weight=1)

start_time = None
curr_sentence=""

label1= Label(text="Click Start to begin", font=("Arial", 24, "bold"), wraplength=400)
label1.grid(row=0,column=1, sticky="ew")

input1 = Entry()
input1.grid(row=1,column=1, sticky="ew")

result_label = Label(text="", font=("Arial", 14))
result_label.grid(row=4, column=1, sticky="ew")

def start_test():
    global start_time, curr_sentence
    curr_sentence = random.choice(SENTENCES)
    label1.config(text=curr_sentence)
    input1.delete(0, END)
    result_label.config(text="")
    start_time = time.time()

def check_test(event):
    typed_text = input1.get()
    if typed_text == curr_sentence:
        end_time = time.time()
        elapsed_seconds = end_time - start_time
        elapsed_minutes = elapsed_seconds / 60

        word_count = len(curr_sentence.split())
        wpm = word_count / elapsed_minutes if elapsed_minutes > 0 else 0

        result_label.config(
            text= f"Time: {elapsed_seconds:.1f}s | WPM: {wpm:.1f} | Accuracy: 100%"
        )

input1.bind("<KeyRelease>", check_test)
start_btn = Button(text="Start", command=start_test)
start_btn.grid(row=2,column=1)

window.mainloop()
