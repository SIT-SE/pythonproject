# note program need install xlrd
import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox, ttk
import checkdataframes

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
file_frame.place(height=100, width=300, rely=0.7, relx=0.01)

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
search_button.pack()
search_button.place(x=300, y=525, height=50, width=80)

# quit button
quit_button = tk.Button(root, text="Quit", command=lambda: destroy())
quit_button.pack(side=tk.BOTTOM, pady=5, ipady=5, ipadx=5)


def destroy():
    root.destroy()


"""# label to open graphing tool
analyse_label = tk.LabelFrame(root, text="Open webpage to view charts")
analyse_label.place(height=100, width=200, x=600, y=415)

# button to open graphing tool
analyse_button = tk.Button(root, text="Open webpage", command=lambda: analyse_data())
analyse_button.pack()
analyse_button.place(x=650, y=440, height=50, width=100) """

# label to open browser
openweb_label = tk.LabelFrame(root, text="Open webpage to view charts")
openweb_label.place(height=100, width=200, x=600, y=400)

# button to open webbrowser
openweb_button = tk.Button(root, text="Open webpage", command=lambda: openweb())
openweb_button.pack()
openweb_button.place(x=650, y=425, height=50, width=100)
new = 1
url = "https://www.google.com"
def openweb():
    webbrowser.open(url, new=new)


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

""" Open new window to search data """
def search_cri():
    file_path = Selected_FLabel["text"]
    column_names = checkdataframes.get_columns(file_path)
    search_data = tk.Tk()
    search_data.title("Search data")
    search_data.geometry("800x600")  # set the root dimensions
    search_data.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
    search_data.resizable(0, 0)  # makes the root window fixed in size.

    def search_now():
        selected = drop.get()
        data_frame = checkdataframes.checkfiletype(file_path)
        searched = search_box.get()
        print(type(data_frame[selected]))
        searched_df = data_frame[data_frame[selected].astype(str).str.contains(searched)]
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

    # Frame for TreeView Data search
    Search_Frame = tk.LabelFrame(search_data, text="Search Criterion")
    Search_Frame.place(height=100, width=500, relx=0.01)
    # Entry box to search data
    search_box = tk.Entry(Search_Frame)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    # Search box label search for customer
    search_box_label = tk.Label(Search_Frame, text="Search Data: ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    # Entry box search Button customer
    search_button = tk.Button(Search_Frame, text="Search", command=search_now)  # add command
    search_button.grid(row=1, column=0, padx=10)

    # Drop down Box
    drop = ttk.Combobox(Search_Frame, values=column_names)
    drop.current(0)
    drop.grid(row=0, column=2)

    # Frame for TreeView Data search
    Tree2_Frame = tk.LabelFrame(search_data, text="Search Data")
    Tree2_Frame.place(height=370, width=785, rely=0.20, relx=0.01)

    # Tree view 2 widget in my 1st frame
    Tree_View2 = ttk.Treeview(Tree2_Frame)
    Tree_View2.place(relheight=1, relwidth=1)

    # Scrolling bar to fit more data in
    TVScroll_y = tk.Scrollbar(Tree2_Frame, orient='vertical', command=Tree_View2.yview)  # scolling feauture for y
    TVScroll_x = tk.Scrollbar(Tree2_Frame, orient='horizontal', command=Tree_View2.xview)
    Tree_View2.configure(xscrollcommand=TVScroll_x.set, yscrollcommand=TVScroll_y.set)
    # Pack these in side
    TVScroll_x.pack(side='bottom', fill='x')
    TVScroll_y.pack(side='right', fill='y')

    # Frame for TreeView Export
    Export_Frame = tk.LabelFrame(search_data, text="Export Data")
    Export_Frame.place(height=100, width=250, rely=0.82, relx=0.35)
    # Entry box to export file name
    export_box = tk.Entry(Export_Frame)
    export_box.grid(row=0, column=1, padx=5, pady=5)
    # Search box label search for customer
    export_box_label = tk.Label(Export_Frame, text="Search Data: ")
    export_box_label.grid(row=0, column=0, padx=10, pady=10)
    # Export button
    export_button = tk.Button(Export_Frame, text="Export to excel", command=lambda: export())  # add command
    export_button.grid(row=1, column=0, padx=5, pady=5)

    # back button
    back_button = tk.Button(Export_Frame, text="Back", command=lambda: back())
    back_button.grid(row=1, column=1, padx=5, pady=5)

    def back():
        search_data.destroy()

    def export():
        export_to = export_box.get()
        selected = drop.get()
        data_frame = checkdataframes.checkfiletype(file_path)
        searched = search_box.get()
        searched_df = data_frame[data_frame[selected].astype(str).str.contains(searched)]
        searched_df.to_excel(export_to + ".xlsx")
        return None


""" Open new window to analyse data """


def analyse_data():
    file_path = Selected_FLabel["text"]
    column_names = checkdataframes.get_columns(file_path)
    analyse_data = tk.Tk()
    analyse_data.title("Search data")
    analyse_data.geometry("800x600")  # set the root dimensions
    analyse_data.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
    analyse_data.resizable(0, 0)  # makes the root window fixed in size.

    # Frame for analyse columns 
    Search_Frame = tk.LabelFrame(search_data, text="Search Criterion")
    Search_Frame.place(height=100, width=500, relx=0.01)


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
