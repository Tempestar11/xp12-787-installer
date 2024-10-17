import os, tkinter as tk
from tkinter import filedialog, messagebox, ttk
from center import center
from PIL import Image, ImageTk
from install import download_plane

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
tabControl.pack(expand = 1, fill ="both", padx = 10, pady = 10) 

# Load, resize, and display an image in the aircraftTab
image_path = "xp12-787-installer/thumbnail.jpg"  # Replace with the path to your image file
image = Image.open(image_path)

# Resize the image to fit within the tab dynamically based on window size
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image_copy = image.copy()
    image_copy.thumbnail((new_width, new_height))
    photo = ImageTk.PhotoImage(image_copy)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection

aircraftTab.bind('<Configure>', resize_image)

photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(aircraftTab, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.grid(column=0, row=0, rowspan=10, columnspan=10, padx = 10, pady = 10)

# Creating a label for xp directory
aircraftLabel = ttk.Label(aircraftTab, text = 'Select X-plane folder: ')
aircraftLabel.grid(column=0, row=10, padx = 10, pady = 10, sticky = 'W')
dirLabel = ttk.Label(aircraftTab, text = 'Selected directory: ')
dirLabel.grid(column=0, row=11, padx = 10, pady = 10, sticky = 'W')

# Creating a label to display the selected directory
selected_dir = tk.StringVar()
selected_dir.set('No directory selected')
dirLabel = ttk.Label(aircraftTab, textvariable = selected_dir)
dirLabel.grid(column=1, row=11, padx = 10, pady = 10, sticky = 'W')

# Creating a button to select the X-plane directory
xp_dir = ''
def select_directory():
    xp_dir = filedialog.askdirectory()
    if xp_dir:
        selected_dir.set(xp_dir)
        show_install_button()
button = ttk.Button(aircraftTab, text = 'Select directory', command = select_directory)
button.grid(column=1, row=10, padx = 10, pady = 10, stick = 'W')

# Creating the install button
button2 = ttk.Button(aircraftTab, text='Install', command = lambda: download_plane(xp_dir))
button2.grid(column=8, row=11, padx=10, pady=10, sticky='E')
button2.grid_remove()  # Initially hide the button

def show_install_button():
    button2.grid()  # Show the button

if __name__ == '__main__':
    root.mainloop()