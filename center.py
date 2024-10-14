import tkinter as tk

def center(root):
# Update the window to get the correct width and height
    root.update_idletasks()

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Get the window width and height
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Calculate the position to center the window
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)

    # Set the window geometry to center it
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_down}')