from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

df = pd.read_csv("data/french_words.csv")
result = df.to_dict(orient="records")

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_id = canvas.create_image(400, 263, image=card_front_img)
title_id = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_id = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


def next_card():
    current_card = random.choice(result)
    canvas.itemconfig(title_id, text=f"French", fill="black")
    canvas.itemconfig(word_id, text=current_card["French"])
    canvas.itemconfig(card_id, image=card_front_img)
    delay()


def flip_card():
    canvas.itemconfig(title_id, text="English", fill="white")
    canvas.itemconfig(card_id, image=card_back_img)


def delay():
    window.after(3000, flip_card)


cross_image = PhotoImage(file="images/wrong.png")
uk_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
uk_btn.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=next_card)
known_btn.grid(row=1, column=1)

next_card()


window.mainloop()
