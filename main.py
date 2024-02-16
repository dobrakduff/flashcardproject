import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


words={}
current_card = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_cart():
    global current_card
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text = "French",fill="black")
    canvas.itemconfig(card_word,text= current_card["French"],fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text= "English", fill="white")
    canvas.itemconfig(card_word,text= current_card["English"], fill="white")
    canvas.itemconfig(card_bg,image=card_back_img)


def is_know():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_cart()


window = Tk()
window.title("Flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)


canvas = Canvas(height=526,width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


yes = PhotoImage(file="images/right.png")
button_y = Button(image=yes, highlightthickness=0,command=next_cart)
button_y.grid(row=1,column=0)


no = PhotoImage(file="images/wrong.png")
button_n = Button(image=no, highlightthickness=0,command=is_know)
button_n.grid(row=1,column=1)


next_cart()


window.mainloop()