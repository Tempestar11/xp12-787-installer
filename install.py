import gdown
import zipfile
import os
import tkinter as tk
from tkinter import messagebox

# Downloads a zipped file from Google Drive to XP-aircraft directory
def download_plane(xp_dir):
    try:
        url = 'https://drive.google.com/uc?1fVlRZooY5W1894rZisCm0s5HYMSDulRs'
        output = os.path.join(xp_dir, '787.zip')
        gdown.download(url, output, quiet=False)
        unzip(os.path.join(xp_dir, '787.zip'), xp_dir)
    except:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Download Error", "Failed to download or unzip the file.")

# Unzips the downloaded file directly to the XP-aircraft directory
def unzip(path_to_zip, xp_dir):
    try:
        with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
            zip_ref.extractall(xp_dir)
    except:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Download Error", "Failed to download or unzip the file.")