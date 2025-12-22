BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_card={}
to_learn={}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("/Users/admin/PycharmProjects/Flash_Cards/data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer= window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    global current_card
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)

    data.to_csv("words_to_learn.csv")
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, next_card)



canvas =Canvas(width=800,height=526)
card_front_img=PhotoImage(file="/Users/admin/PycharmProjects/Flash_Cards/images/card_front.png")
card_back_img=PhotoImage(file="/Users/admin/PycharmProjects/Flash_Cards/images/card_back.png")
card_background=canvas.create_image(400, 263,image=card_front_img)
card_title=canvas.create_text(400,150, text="Title", font=("Arial", 40,"italic"), fill="black")
card_word=canvas.create_text(400,263, text="word", font=("Arial", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)



#buttons
cross_img=PhotoImage(file="/Users/admin/PycharmProjects/Flash_Cards/images/wrong.png")
unknown_button=Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_img=PhotoImage(file=r"/Users/admin/PycharmProjects/Flash_Cards/images/right.png")
check_button=Button(image=check_img,highlightthickness=0 , command=is_known)
check_button.grid(row=1,column=1)
next_card()

window.mainloop()

