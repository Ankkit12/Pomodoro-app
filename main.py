from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = N
count_min = 0
count_sec = 0
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    """This function resets the timer"""
    window.after_cancel(timer)
    title_label.config(text="Timer")
    checkmark_label.config(text="")
    canvas.itemconfigure(timer_text, text="00:00")
    global reps
    reps = 0


# def stop():
#     global count_min
#     global count_sec
#     count_min = 0
#     count_sec = 0
#     """This function stops the timer"""
#     canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
#     return True





# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """This function does the work of starting the timer"""
    global reps
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps = reps + 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", foreground=RED)
        return reps
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", foreground=PINK)
        return reps
    else:
        count_down(work_min_sec)
        title_label.config(text="Work", foreground=GREEN)
        return reps

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    # if stop:
    #     print("stop")
    #     break
    # else:
    global count_min
    global count_sec

    """This function does the work of counting the seconds and minutes"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------ #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 50), foreground=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
#
# stop_button = Button(text="stop", highlightthickness=0, command=stop)
# stop_button.grid(row=2, column=1)

checkmark_label = Label(foreground=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
