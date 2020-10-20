import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os.path

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    # output based on user-defined columns. * work on this
    print (df.iloc[:,[2,3,4]])

def checkFileName(filename):

    #check export file for special characters or blank input.  
    special_char = ".!@#$%^&*()-+"
    
    if filename == "":
        print("Invalid file name! Please enter another file name, don't leave it blank this time :)")
            
        return False
        
    elif any(c in special_char for c in filename):
        print("You have entered an invalid filename with special characters! Run the program again.")
            
        return False

#    elif os.path.exists(filename):
#        print("A file with the same name already exists. Pleas enter a different file name.")
        
#        return False
    else:
        return True
         
    

# function to export to excel. currently, only available to local directory, work on specific filepath.
def exportExcel():
    # check export file for special characters or blank input.
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel(import_file_path)

    # allow users to select columns
    selectCol = list(input("Select the columns you want to output:"))
    colList = [str(i) for i in selectCol]
    joined = ",".join(colList)

    # need additional work on selecting specific columns
    df1 = df.iloc[:,[1]]   
    
    # user-defined file name.
    filename = input("Please specify a name for your file.\n Do not use special characters such as '.!@#$%^&*()-+' (excluding the file extension): ")
    
    if checkFileName(filename) == False:
        #need to find out a way to run program again.
        exit()

    else:
        # allow user to specify filename, then append to .xlsx
        writer = pd.ExcelWriter(filename +".xlsx", engine='xlsxwriter')
        df1.to_excel(writer, sheet_name='Sheet1')

        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']

        # Add some cell formats.
        format1 = workbook.add_format({'num_format': '#,##0.00'})
        format2 = workbook.add_format({'num_format': '0%'})

        # Note: It isn't possible to format any cells that already have a format such
        # as the index or headers or any cells that contain dates or datetimes.

        # Set the column width and format.
        worksheet.set_column('B:B', 18, format1)

        # Set the format but not the column width.
        worksheet.set_column('C:C', None, format2)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        print(filename + ".xlsx successfully saved!")


# have to work on using this file path to export to selected directory
def getFilePath():

    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window

    currdir = os.getcwd()
    tempdir = fd.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

    if len(tempdir) > 0:
        print ("You chose %s" % tempdir)


#browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
exportButton_Excel = tk.Button(text='Export your results', command=exportExcel, bg='blue', fg = 'white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(150, 150, window=browseButton_Excel)
canvas1.create_window(150, 150, window=exportButton_Excel)

root.mainloop()