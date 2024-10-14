import os, tkinter as tk
from tkinter import filedialog, messagebox, ttk
from center import center
from PIL import Image, ImageTk

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
image_path = "thumbnail.jpg"  # Replace with the path to your image file
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
image_label.grid(column=0, row=0)

# Creating a label for the aircraft installer
aircraftLabel = ttk.Label(aircraftTab, text = 'Select X-plane folder: ')
aircraftLabel.grid(column=0, row=1, padx = 10, pady = 10, sticky = 'W')


# Creating a button to select the X-plane directory
def select_directory():
    xp_dir = filedialog.askdirectory()
    if xp_dir:
        messagebox.showinfo('Selected directory', f'You selected: {xp_dir}')

button = ttk.Button(aircraftTab, text = 'Select directory', command = select_directory)
button.grid(column=0, row=1, padx = 10, pady = 10)

if __name__ == '__main__':
    root.mainloop()