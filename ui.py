import tkinter as tk
import time

def afkStart():
    pass

def afkStop():
    pass









window = tk.Tk()

window.config(height=600, width=600)

afkStartButton = tk.Button(command=afkStart, text="Start!")
afkStartButton.config(height=4, width=10)
afkStartButton.place(x=300, y=280)

afkStopButton = tk.Button(command=afkStop, text="Stop!")
afkStopButton.config(height=4, width=10)
afkStopButton.place(x=215, y=280)




window.mainloop()
