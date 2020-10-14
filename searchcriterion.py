"""Using pandas lib to search information from rows"""
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk





def read_data(file_path):
    filename = r"{}".format(file_path)
    if ".xlsx" in filename:
        data_frame = pd.read_excel(filename)
    elif ".json" in filename:
        data_frame = pd.read_json(filename)
    elif ".csv" in filename:
        data_frame = pd.read_csv(filename)
    elif ".txt" in filename:
        data_frame = pd.read_csv(filename)
    else:
        print("Error")
    column_list = list(data_frame.columns.values)

    return column_list


