import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter MessageBox')
root.resizable(False, False)
root.geometry('300x150')

#
options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

def displayError(text):
    ttk.Button(
        root,
        text,
        command=lambda: showerror(
        title='Error',
        message='This is an error message.')
        ).pack(**options)
    root.mainloop()


def displayInformation(text):
    ttk.Button(
        root,
        text,
        command=lambda: showinfo(
        title='Information',
        message='This is an information message.')
        ).pack(**options)
    root.mainloop()


def displayWarning(text):
    ttk.Button(
        root,
        text='Show an warning message',
        command=lambda: showwarning(
        title='Warning',
        message='This is a warning message.')
        ).pack(**options)
    root.mainloop()