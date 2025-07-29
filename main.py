"""
Author: Brandan Zmegac
Date Modified: 19/3/2025
Version 0.0
This program will allow the user to effortlessly create and edit Journal Entries, Lists, and Reminders.
"""

# Import

import tkinter as tk
from tkinter import *

# Functions



# Classes

class ScrollBarDemo:

    def __init__(self):
        scrollBarVertical = Scrollbar(master=mainFrame)
        scrollBarVertical.pack(side=RIGHT, fill=Y)
        sampleText = Text(master=mainFrame, width=30, height=30, wrap=WORD,
                 yscrollcommand=scrollBarVertical.set)
        for i in range(1):
            sampleText.insert(END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n")
        sampleText.pack(side=TOP, fill=X)
        scrollBarVertical.config(command=sampleText.yview)
        mainFrame.mainloop()

# GUI

    # Main Window

mainWindow = tk.Tk()
mainWindow.title("Journal Program")
mainWindow.geometry("800x600")

mainWindow.rowconfigure(0, minsize=100, weight=1)
mainWindow.columnconfigure(0, minsize=200, weight=1)
mainWindow.resizable(width=False, height=False)

    # Main Frame

mainFrame = tk.Frame(master=mainWindow, relief=tk.RAISED, borderwidth=3)



    # Main Workspace



    # Left Workspace

leftFrame = tk.Frame(master=mainFrame, relief=tk.RAISED, borderwidth=3)
leftFrame.grid(row=1,column=1)
mainFrame.pack()





s = ScrollBarDemo()

    # Right Workspace


# Run


mainWindow.mainloop()
