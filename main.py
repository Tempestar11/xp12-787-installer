import os, tkinter as tk
from tkinter import filedialog, messagebox, ttk
from center import center
from PIL import Image, ImageTk
from install import download_plane
import threading
from image_loading import load_image, display_image

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

# Function to load the image in a separate thread
def load_image_thread():
    global image
    image_path = "xp12-787-installer/thumbnail.jpg"  # Replace with the path to your image file
    image = load_image(image_path)

# Function to check if the image has been loaded and update the GUI
def check_image_loaded():
    if 'image' in globals():
        display_image(aircraftTab, image)
    else:
        aircraftTab.after(100, check_image_loaded)

# Start the image loading in a separate thread
threading.Thread(target=load_image_thread).start()
# Periodically check if the image has been loaded
aircraftTab.after(100, check_image_loaded)

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
button.bind('<Enter>', lambda e: button.config(cursor='hand2'))
button.bind('<Leave>', lambda e: button.config(cursor='arrow'))

# Creating the install button
button2 = ttk.Button(aircraftTab, text='Install', command = lambda: download_plane(xp_dir))
button2.grid(column=8, row=11, padx=10, pady=10, sticky='E')
button2.grid_remove()  # Initially hide the button

def show_install_button():
    button2.grid()  # Show the button
    button2.bind('<Enter>', lambda e: button.config(cursor='hand2'))
    button2.bind('<Leave>', lambda e: button.config(cursor='arrow'))

if __name__ == '__main__':
    root.mainloop()