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
        countdown(5)
        eraser = False


def reset_timer():
    global eraser
    window.after_cancel(timer)
    countdown(5)


def countdown(count):
    global written_text
    check_text()
    if count < 10:
        count = f"0{count}"
    canvas.itemconfig(timer_text, text=f"{count}")
    if int(count) > 0:
        global timer
        timer = window.after(1000, countdown, int(count) - 1)
    elif int(count) == 0:
        # TODO create a function that saves your work in a text file first
        text.delete("1.0", END)
        written_text = text.get(1.0, END)
        countdown(5)


# TODO should instead stop timer from moving when it restarts
def check_text():
    global written_text
    current_text = text.get(1.0, END)
    if written_text == current_text:
        pass
    else:
        written_text = current_text
        reset = window.after(250, reset_timer)


canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="20", fill="white", font=("Georgia", 35, "bold"))
# time_label = tk.Label(text="20", font=("Georgia", 20))
# time_label.grid(row=0, column=0, sticky="nsew")
canvas.grid(row=0, column=0, sticky="nsew")
text = tk.Text(height=20, width=30)
text.configure(font=('TimesNewRoman', 13))
text.grid(row=1, column=0, rowspan=2)

placeholder_text = "Time to write or die!"
text.insert(1.0, placeholder_text)
text.bind("<Button-1>", lambda event: clear_text(event, text))


window.mainloop()
