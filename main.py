from tkinter import *
import tkinter as tk


class WindowManager:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Write or Die!")
        self.window.geometry("600x400")
        self.eraser = True
        self.timer = ""
        self.written_text = ""

        self.canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
        self.timer_text = self.canvas.create_text(100, 130, text="20", fill="white", font=("Georgia", 35, "bold"))
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.text = tk.Text(height=20, width=30)
        self.text.configure(font=('TimesNewRoman', 13))
        self.text.grid(row=1, column=0, rowspan=2)

        self.placeholder_text = "Time to write or die!"
        self.text.insert(1.0, self.placeholder_text)
        self.text.bind("<Button-1>", lambda event: self.clear_text(event, self.text))
        self.window.mainloop()

    def clear_text(self, event, my_text):
        if self.eraser:
            my_text.delete("1.0", END)
            my_text.unbind('<Button-1>', "event")
            self.countdown(5)
            self.eraser = False

    def resume_countdown(self, an_event, my_text):
        if True:
            my_text.unbind("an_event")
            self.reset_timer()

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.countdown(5)

    def countdown(self, count):
        current_text = self.check_text()
        if count < 10:
            count = f"0{count}"
        self.canvas.itemconfig(self.timer_text, text=f"{count}")
        if int(count) > 0:
            self.timer = self.window.after(1000, self.countdown, int(count) - 1)
        elif int(count) == 0 and len(current_text) != 0:
            # TODO create a function that saves your work in a text file first
            self.text.delete("1.0", END)
            self.written_text = self.text.get(1.0, END)
            self.text.bind("<KeyRelease>", lambda an_event: self.resume_countdown(an_event, self.text))
        else:
            self.text.bind("<KeyRelease>", lambda an_event: self.resume_countdown(an_event, self.text))

    def check_text(self):
        current_text = self.text.get(1.0, "end-1c")
        if self.written_text == current_text:
            return current_text
        else:
            self.written_text = current_text
            return 'Not blank'


wm = WindowManager()
