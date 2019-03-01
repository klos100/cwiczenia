import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

exportFile = tkFileDialog.asksaveasfile(mode='a')
exportFile.name

# import csv
#     import pandas as pd
#     import os
#     import tkinter as tk
#     from tkinter import filedialog
#
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename()
#     dataFile=pd.read_csv(file_path,usecols=['Name','Email','Gender'])
#     SAVING_PATH = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
#     dataFile.to_csv(SAVING_PATH)