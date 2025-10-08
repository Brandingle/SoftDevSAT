"""
Author: Brandan Zmegac
Date Modified: 19/3/2025
Version 0.0
This program will allow the user to effortlessly create and edit Journal Entries, Lists, and Reminders.
"""

# Import - Imports various libraries etc, to allow for more functionality in the code, for example: GUI from Tkinter.

import tkinter as tk # Gives tkinter a simpler name
from tkinter import * # Imports all available Tkinter functions.

# Files - Files used in the program

# saveButtonImage = (Spare unused code to open the Save Button's image)

# Functions - Functions to give the code functionality (Obviously!)

    # Tests - Various Functions used for testing programming components

# Note: Could be consolidated. Maybe a class that goes based on the tested function/areas name to reduce code?

def saveButtonTest(): # Tests the Save Button in the Button Box
    print("Save Button Pressed")

def settingsButtonTest(): # Tests the Settings Button in the Button Box
    print("Settings Button Pressed")

def warningButtonTest(): # Tests the Warning Button in the Button Box
    print("Warning Button Pressed")

def exportButtonTest(): # Tests the Export Button in the Button Box
    print("Export Button Pressed")


# Classes

class mainWorkspace: # Provides interactive text workspace for the Main Workspace GUI.

    def __init__(self):
        scrollBarVertical = Scrollbar(master=mainWorkFrame)
        scrollBarVertical.pack(side=RIGHT, fill=Y)
        textBox = Text(master=mainWorkFrame, width=52, height=29, wrap=WORD,
                 yscrollcommand=scrollBarVertical.set)
        for i in range(1):
            textBox.insert(END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n")
        textBox.pack(side=TOP, fill=X)
        scrollBarVertical.config(command=textBox.yview)
        lowerMainFrame.mainloop()

class rightWorkspace: # Provides interactive workspace for the Right Workspace GUI.

    def __init__(self):
        scrollBarVertical = Scrollbar(master=rightWorkFrame)
        scrollBarVertical.pack(side=RIGHT, fill=Y)
        textBox = Text(master=rightWorkFrame, width=10, height=10, wrap=WORD,
                 yscrollcommand=scrollBarVertical.set)
        for i in range(1):
            textBox.insert(END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam, ac elementum nunc imperdiet eu. Aenean a libero nec magna tincidunt ornare a eu lacus. Curabitur sed metus et diam varius consequat. Aenean purus eros, commodo ac pretium nec, pretium ac nulla. Ut sit amet pharetra lacus, a scelerisque velit. Nullam pellentesque, tortor sit amet tincidunt sollicitudin, purus augue tincidunt ante, eget porttitor nulla nunc sit amet enim. Quisque ultricies nisi nec quam mollis imperdiet. Vivamus ligula leo, cursus sit amet porta nec, vulputate et felis. Curabitur tellus mauris, interdum sed aliquam ac, dignissim in mauris.\n")
        textBox.pack(side=TOP, fill=X)
        scrollBarVertical.config(command=textBox.yview)
        lowerMainFrame.mainloop()

# GUI - Visible components of the program that the user will see and interact with.

    # Main Window - The main window that has the 'Journal Program' title, and contains all subsequent GUI elements, buttons, etc...

mainWindow = tk.Tk()
mainWindow.title("Journal Program")
mainWindow.geometry("700x500")

mainWindow.rowconfigure(0, minsize=100, weight=1)
mainWindow.columnconfigure(0, minsize=200, weight=1)
mainWindow.resizable(width=False, height=False)

        # Upper Main Frame - Houses the title and description, main buttons, menus, reminders, and subsequent GUI elements.

upperMainFrame = tk.Frame(master=mainWindow, relief=tk.RAISED, borderwidth=3, width=791, height=100)
upperMainFrame.grid(row=0,column=0)

            # Title and Description Box - Displays the title and description of the current open file (Journal/List), as well as other information such as the time of creation and/or last edit.

titleDescBox = tk.Frame(master=upperMainFrame, relief=tk.SUNKEN,borderwidth=3, width=150, height=100)
titleDescBox.grid(row=0, column=0)

            # Reminder Workspace - A small static workspace where the user can write reminders or other small, priority notes.

reminderWorkspace = tk.Frame(master=upperMainFrame, relief=tk.RAISED,borderwidth=3, width=300, height=100)
reminderWorkspace.grid(row=0, column=1)

            # Button Box - Contains the save, settings, warning, and export buttons.

buttonBox = tk.Frame(master=upperMainFrame, borderwidth=3, width=100, height=100)
buttonBox.grid(row=0, column=2)

                # Save Button - When clicked displays save menu.

# !! Below code is not yet implemented !!
# Code will add image to save button
# (Will be implemented to other buttons in Button Box)

#saveButtonFrame = tk.Frame(master=buttonBox, relief=tk.RAISED, borderwidth=3, width=5, height=5)
#buttonBox.grid(row=0, column=2)

#saveButtonLogo = PhotoImage(file = r"/Users/26bzmegac/Downloads/529448B7-1362-4451-BD80-8BFBA8489F45-removebg-preview.png") - See look I technically almost used a file.
#saveLogo = saveButtonLogo.subsample(100,100)

saveButton = tk.Button(master=buttonBox, borderwidth=1, width=1, height=2, cursor="hand2", command=saveButtonTest)
saveButton.grid(row=0,column=0)

                # Settings Button - When clicked displays settings menu.

settingsButton = tk.Button(master=buttonBox, borderwidth=1, width=1, height=2, cursor="hand2", command=settingsButtonTest)
settingsButton.grid(row=0,column=1)

                # Warning Button - Shows current file status, image on button changes based on status, when clicked will show brief description and/or error code for the issue (Status/Error window).

# Note (To be added): Show status as text when hovered over with mouse.

warningButton = tk.Button(master=buttonBox, borderwidth=1, width=1, height=2, cursor="hand2", command=warningButtonTest)
warningButton.grid(row=1,column=0)

                # Export Button - When clicked opens the export menu window.

exportButton = tk.Button(master=buttonBox, borderwidth=1, width=1, height=2, cursor="hand2", command=exportButtonTest)
exportButton.grid(row=1,column=1)

            # Time and Date Box - Contains the user's current time and date.

timeDateBox = tk.Frame(master=upperMainFrame, relief=tk.SUNKEN,borderwidth=3, width=150, height=100)
timeDateBox.grid(row=0, column=3)

        # Lower Main Frame - Contains Left Menu, Main Workspace, and Right Workspace.

lowerMainFrame = tk.Frame(master=mainWindow, relief=tk.RAISED, borderwidth=3)
lowerMainFrame.grid(row=1,column=0)

        # Main Workspace - The main workspace where the user can write large notes or journal entries

mainWorkFrame = tk.Frame(master=lowerMainFrame, relief=tk.RAISED, borderwidth=3)
mainWorkFrame.grid(row=1,column=1)

        # Left Menu - A scrollable menu which shows available project files (Journals/Lists) that the user can look through and open into the main workspace, as well as an option to create a new project file.

leftMenu = tk.Frame(master=lowerMainFrame, relief=tk.RAISED, borderwidth=3, width=150, height=391)
leftMenu.grid(row=1,column=0)

        # Right Workspace - A smaller static workspace where users can write small notes such as passwords or dates.

rightWorkFrame = tk.Frame(master=lowerMainFrame, relief=tk.RAISED, borderwidth=3, width=150, height=391)
rightWorkFrame.grid(row=1,column=2)

# !! Below code is not yet implemented !!
# Code will add workspace to Right Workspace, currently working out formatting errors.
# (Will be implemented to other workspaces in Button Box)

    #rightWorkText = tk.Text(master=rightWorkspace, relief=tk.RAISED, borderwidth=3, wrap=WORD)
    #rightWorkText.insert(END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin cursus pellentesque quam\n")
    #rightWorkText.pack()


# Run - Basic commands to start the program when run.

s = mainWorkspace()
d = rightWorkspace()
mainWindow.mainloop()


