from tkinter import *
import time
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text='')
    global reps
    reps=0


def star_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8 == 0:
        title_label.config(text="Long break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)




def count_down(count):
    global reps
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer=window.after(1000,count_down,count-1)
    else:
        star_timer()
        mark=''
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark+='✔️'
        check_mark.config(text=mark)


window = Tk()
window.title("Pomidoro")
window.config(bg=YELLOW)
window.config(padx=100, pady=50, bg=YELLOW)

title_label=Label(text="Timer", fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)  # центр картинки
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", fg=GREEN, bg=YELLOW, highlightthickness=0,command=star_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=GREEN, bg=YELLOW, highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark=Label(text="✅", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=3)




window.mainloop()