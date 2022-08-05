from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)


def reset():
    window.after_cancel(timer)
    check_mark.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


def count_down(count):
    global timer
    global reps
    if count >= 0:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if 0 <= count_sec < 10:
            count_sec = "0" + str(count_sec)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
        # The timer would take count - 1 as a parameter for the count down method
    else:
        start_timer()
        marks = ""
        number_of_completion = math.floor(reps / 2)
        for _ in range(number_of_completion):
            marks += "✔"

        check_mark.config(text=f"{marks}")


timer_label = Label(text="Timer", font=(FONT_NAME, 30, "normal"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 122, fill="white", text="00.00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
