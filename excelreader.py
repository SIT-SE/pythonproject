# Imports
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():
    pass


def clear_data():
    pass
