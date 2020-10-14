# note program need install xlrd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import checkdataframes
import searchcriterion
import pandas as pd

"""GUI code"""
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
file_frame.place(height=100, width=300, rely=0.65, relx=0)

# Buttons to read excel files
browse_button = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
browse_button.place(rely=0.65, relx=0.50)

load_button = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
load_button.place(rely=0.65, relx=0.30)

# The file/file path text
Selected_FLabel = ttk.Label(file_frame, text="No File Selected")
Selected_FLabel.place(rely=0, relx=0)

# Search Criterion
search_button = tk.Button(root, text="Search Data", command=lambda: search_cri())
search_button.pack(side=tk.BOTTOM)


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


def search_cri():
    file_path = Selected_FLabel["text"]
    column_names = checkdataframes.get_columns(file_path)
    search_data = tk.Tk()
    search_data.title("Search data")
    search_data.geometry("800x600")  # set the root dimensions



    def search_now():
        selected = drop.get()
        data_frame = checkdataframes.checkfiletype(file_path)
        searched = search_box.get()
        searched_df = data_frame[data_frame[selected].str.contains(searched)]
        print(searched_df)
        Tree_View2["column"] = list(searched_df.columns)
        # Show only the headings
        Tree_View2["show"] = "headings"
        for column in Tree_View2["column"]:
            Tree_View2.heading(column, text=column)  # let the column heading = column name
        # turns the dataframe into a list of lists
        searched_df_rows = searched_df.to_numpy().tolist()
        # inserts each list into the treeview
        for row in searched_df_rows:
            Tree_View2.insert("", "end", values=row)
        return None

    # Entry box to search data
    search_box = tk.Entry(search_data)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    # Search box label search for customer
    search_box_label = tk.Label(search_data, text="Search Data: ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    # Entry box search Button customer
    search_button = tk.Button(search_data, text="Search", command=search_now)  # add command
    search_button.grid(row=1, column=0, padx=10)

    # Drop down Box
    drop = ttk.Combobox(search_data, values=column_names)
    drop.current(0)
    drop.grid(row=0, column=2)

    # Frame for TreeView Data search
    Tree2_Frame = tk.LabelFrame(search_data, text="Search Data")
    Tree2_Frame.grid(row=3, column=0)

    # Tree view 2 widget in my 1st frame
    Tree_View2 = ttk.Treeview(Tree2_Frame)
    Tree_View2.grid(row=3, column=0)



"""Functions for uploading files"""


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("text files", "*.txt"),
                                                    ("csv files", "*.csv"), ("json files", "*.json"),
                                                    ("All Files", "*.*")))
    Selected_FLabel["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = Selected_FLabel["text"]
    try:
        data_frame = checkdataframes.checkfiletype(file_path)
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
