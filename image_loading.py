from PIL import Image, ImageTk
from tkinter import ttk

def load_image(image_path):
    # Load the image
    image = Image.open(image_path)
    return image

def display_image(aircraftTab, image):
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
    image_label.grid(column=0, row=0, rowspan=10, columnspan=10, padx=10, pady=10)