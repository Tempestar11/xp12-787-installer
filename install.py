import gdown
import zipfile
import os

# Downloads a zipped file from Google Drive to XP-aircraft directory
def download_plane(xp_dir):
    url = 'https://drive.google.com/uc?1fVlRZooY5W1894rZisCm0s5HYMSDulRs'
    output = os.path.join(xp_dir, '787.zip')
    gdown.download(url, output, quiet=False)
    # If file is zipped
    unzip(os.path.join(xp_dir, '787.zip'), xp_dir)

# Unzips the downloaded file directly to the XP-aircraft directory
def unzip(path_to_zip, xp_dir):
    with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
        zip_ref.extractall(xp_dir)