"""
Simple typing test application

random words list from
https://www.randomlists.com/random-words?dup=false&qty=300#google_vignette
"""


import random
import time
import tkinter as tk
from tkinter import ttk, END, CENTER
from threading import Thread


paragraph = ""
text = ""
user_text = ""
current_character = 0
seconds = 0
minutes = 0
running = False
finished = False
num_of_words = 5
wpm = 0
cpm = 0


"""
with open("words.txt", "r") as file:
    word_list = file.readlines()
    for x in range(5):
        text += " " + random.choice(word_list).strip()

text = text[1:]
"""

def add_character(event):
    global text_area
    global running
    global user_text
    global paragraph
    global current_character
    if event.char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_{}[]|:;'<>,.?/abcdefghijklmnopqrstuvwxyz- ":
        if not running:
            running = True
            start_timer()
        temp = user_text + event.char
        if event.char == text[current_character] and temp == text[:(current_character + 1)]:
            paragraph.tag_config("start", foreground="green")
            paragraph.tag_add("start", f"end-{len(text) + 1 - current_character}c", f"end-{len(text) - current_character}c")
        else:
            paragraph.tag_config("start", foreground="red")
            paragraph.tag_add("start", f"end-{len(text) + 1 - current_character}c", f"end-{len(text) - current_character}c")
        user_text += event.char
        current_character += 1
    if ord(event.char) == 8:
        user_text = user_text[:(len(user_text) - 1)]
        current_character -= 1
    if user_text == text:
        finished = True

def start_timer():
    t = Thread(target=timer)
    t.start()


def timer():
    global seconds
    global minutes
    global wpm
    global cpm
    global num_of_words
    global finished
    global current_character
    global text
    global user_text
    time_label = tk.Label(root, text="0:00", bg="black", fg="orange")
    time_label.place(x=520, y=40)
    while not finished:
        time_label.config(text=f"{seconds//60}:{(seconds % 60) // 10}{(seconds % 60) % 10}")
        time.sleep(1)
        seconds += 1
        if user_text == text:
            break
    seconds -= 1
    minutes = seconds / 60
    wpm = num_of_words / minutes
    cpm = len(text) / minutes
    victory_label = tk.Label(root, text=f"time: {seconds}\nwpm: {wpm:.1f}\ncpm: {cpm:.1f}", border=3, \
    relief="solid", font=("Arial", 12))
    victory_label.place(x=245, y=410)
    print(seconds)


root = tk.Tk()
root.geometry("607x500")
root.resizable(width=False, height=False)
root.title("Typing Test")
root.option_add("*tearOff", False)

title_label = tk.Label(root, text="Test your typing speed!", border=3, relief="solid", font=("Arial", 15))
title_label.place(x=201, y=30)

def start():
    global paragraph
    global text
    text = ""
    global user_text
    user_text = ""
    global current_character
    current_character = 0
    global seconds
    seconds = 0
    global minutes
    minutes = 0
    global running
    running = False
    global finished
    finished = False
    global num_of_words
    num_of_words = 30
    global wpm
    wpm = 0
    global cpm
    cpm = 0
    with open("words.txt", "r") as file:
        word_list = file.readlines()
        for x in range(num_of_words):
            text += " " + random.choice(word_list).strip()

    text = text[1:]
    paragraph = tk.Text(root, width=65, height=6)
    paragraph.place(x=40, y=120)
    paragraph.insert(END, text)
    paragraph.config(state="disabled")

    text_area = tk.Text(root, width=65, height=6)
    text_area.place(x=40, y=280)


reset_button = tk.Button(root, text="reset", border=1, fg="green", command=start)
reset_button.place(x=20, y=20)

root.bind("<Key>", add_character)


start()
root.mainloop()

