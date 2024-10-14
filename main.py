import os, tkinter as tk
from tkinter import filedialog, messagebox, ttk
from center import center

# Creating main window
root = tk.Tk()
root.title('XP-12 787 Aircraft Installer')

# Auto resises the window to the screen size
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width*0.5,height*0.5))

# Center the window
center(root)

# Creating tabs for aircraft and livery installers
tabControl = ttk.Notebook(root)

aircraftTab = ttk.Frame(tabControl)
liveryTab = ttk.Frame(tabControl)

tabControl.add(aircraftTab, text ='Aircraft installer') 
tabControl.add(liveryTab, text ='Livery installer') 
tabControl.pack(expand = 1, fill ="both") 

ttk.Label(aircraftTab, text = "Aircraft installer").grid(column = 0, row = 0, padx = 30, pady = 30)   
ttk.Label(liveryTab, text = "Livery installer").grid(column = 0, row = 0, padx = 30, pady = 30) 

if __name__ == '__main__':
    root.mainloop()