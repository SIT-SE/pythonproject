# note program need install xlrd
import checkdataframes
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

# initialised the tkinter GUI
root = tk.Tk()

root.geometry("900x600")  # set the root dimensions
root.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0)  # makes the root window fixed in size.

# Frame for TreeView
Tree_Frame = tk.LabelFrame(root, text="Excel Data")
Tree_Frame.place(height=400, width=900)

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=150, width=400, rely=0.65, relx=0)

# Buttons to read excel files
browse_button = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
browse_button.place(rely=0.65, relx=0.50)

load_button = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
load_button.place(rely=0.65, relx=0.30)

# The file/file path text
Selected_FLabel = ttk.Label(file_frame, text="No File Selected")
Selected_FLabel.place(rely=0, relx=0)

# Tree view widget in my 1st frame
Tree_View1 = ttk.Treeview(Tree_Frame)
Tree_View1.place(relheight=1, relwidth=1)

# Scrolling bar to fit more data in
TVScroll_y = tk.Scrollbar(Tree_Frame, orient='vertical', command=Tree_View1.yview)  # scolling feauture for y
TVScroll_x = tk.Scrollbar(Tree_Frame, orient='horizontal', command=Tree_View1.xview)
Tree_View1.configure(xscrollcommand=TVScroll_x.set, yscrollcommand=TVScroll_y.set)
# Pack these in side
TVScroll_x.pack(side='bottom', fill='x')
TVScroll_y.pack(side='right', fill='y')


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    Selected_FLabel["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = Selected_FLabel["text"]
    try:
        data_frame = pd.read_excel(excel_filename)
    # if the above fail
    except ValueError:
        tk.messagebox.showerror("Information", "The file chosen is invalid!")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No file named {file_path} found!")

    clear_data()
    Tree_View1["column"] = list(data_frame.columns)
    # Show only the headings
    Tree_View1["show"] = "headings"
    for column in Tree_View1["column"]:
        Tree_View1.heading(column, text=column)  # let the column heading = column name
    # turns the dataframe into a list of lists
    dataframe_rows = data_frame.to_numpy().tolist()
    # inserts each list into the treeview
    for row in dataframe_rows:
        Tree_View1.insert("", "end", values=row)
    return None


def clear_data():
    Tree_View1.delete(*Tree_View1.get_children())
    return None


# Create a loop to check for end of program
root.mainloop()
