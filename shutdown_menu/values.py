# !/usr/bin/python3
import os
from functools import partial
import tkinter as tk
from tkinter import ttk

# window width and height
wwdw = 250
hwdw = 100

# click method
def clicked(op: str):
    command = "shutdown "
    if op == "shutdown":
        command += "/s /t 1"
    elif op == "reboot":
        command += "/r /t 1"
    elif op == "hibernate":
        command += "/h"
    os.system(command)
    exit()

# set tkinter button options
def opbutton(root, option, icon):
    return ttk.Button(
        root,
        image=icon,
        text=option,
        compound=tk.TOP,
        command=partial(clicked, option)
    )

# button details
def pack(button):
    return button.pack(
        ipadx=5,
        ipady=5,
        side='left'
    )

# set icon
def icon(op: str):
    return tk.PhotoImage(file='./assets/'+op+'.png')
