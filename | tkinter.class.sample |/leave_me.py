# Standart module of Python is imported as tk

import tkinter as tk

class Test_Window(tk.Tk):
    def __init__(self):
        # In order not to be mixed original __init__ with Tkinter module we use super()
        super().__init__()
        # Defined exit func. will be enable if we try to close with x at the corner of windows 
        self.protocol("WM_DELETE_WINDOWS", self.exit)

        self.tag = tk.Label(text="Let me go!")
        self.tag.pack()

        self.button = tk.Button(text="Let it go.", command=self.exit)
        self.button.pack()

    def exit(self):
        # Func. will be working in order according to lines
        self.tag["text"] = "Bye bye..."
        self.button["text"] = "Leaving..."
        # After click the button it will be inactive
        self.button["state"] = "disabled"
        # window will be dissappear after 2000ms(=2 seconds)
        self.after(2000, self.destroy)

window = Test_Window()
# Size of windows as pixel
window.geometry("400x300")
# Code for command as GUI at Tkinter module 
window.mainloop()
