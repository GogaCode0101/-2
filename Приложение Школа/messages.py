#messages.py

import tkinter as tk
from tkinter import messagebox

def show_error(title, message):
    messagebox.showerror(title, message)

def show_success(title, message):
    messagebox.showinfo(title, message)