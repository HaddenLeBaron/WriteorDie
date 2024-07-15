from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Write or Die!")
window.geometry("600x400")
eraser = True
timer = ""
written_text = ""


def clear_text(event, my_text):
    global eraser
    if eraser:
        my_text.delete("1.0", END)
        my_text.unbind('<Button-1>', "event")
        print('1')
        countdown(5)
        eraser = False


def resume_countdown(an_event, my_text):
    if True:
        my_text.unbind("an_event")
        window.after_cancel(timer)
        print('3')
        countdown(5)


def reset_timer():
    window.after_cancel(timer)
    print('4')
    countdown(5)


def countdown(count):
    global written_text
    current_text = check_text()
    if count < 10:
        count = f"0{count}"
    canvas.itemconfig(timer_text, text=f"{count}")
    if int(count) > 0:
        global timer
        timer = window.after(1000, countdown, int(count) - 1)
    elif int(count) == 0 and len(current_text) != 0:
        # TODO create a function that saves your work in a text file first
        text.delete("1.0", END)
        written_text = text.get(1.0, END)
        print('2')
        countdown(5)
    else:
        text.bind("<KeyRelease>", lambda an_event: resume_countdown(an_event, text))


# TODO should instead stop timer from moving when it restarts
def check_text():
    global written_text
    current_text = text.get(1.0, "end-1c")
    if written_text == current_text:
        return current_text
    else:
        written_text = current_text
        reset = window.after(250, reset_timer)
        return 'Not blank'


canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="20", fill="white", font=("Georgia", 35, "bold"))
canvas.grid(row=0, column=0, sticky="nsew")
text = tk.Text(height=20, width=30)
text.configure(font=('TimesNewRoman', 13))
text.grid(row=1, column=0, rowspan=2)

placeholder_text = "Time to write or die!"
text.insert(1.0, placeholder_text)
text.bind("<Button-1>", lambda event: clear_text(event, text))


window.mainloop()
