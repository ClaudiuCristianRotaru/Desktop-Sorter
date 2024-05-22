import os
from os import walk
import shutil

# Get desktop path (tested only for Windows)
DESKTOP_PATH = desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + '\\'
# Don't try to move these files
NONO_FILES = ["desktop.ini", "SortDesktop.lnk"]
SORTING_FOLDERS = ["Games", "Images", "Programs", "Files"]
folders = []
files = []
for (dirpath, dirnames, filenames) in walk(DESKTOP_PATH):
    files.extend(filenames)
    folders.extend(dirnames)
    break

for nono_file in NONO_FILES:
    files.remove(nono_file)

for sorting_folder in SORTING_FOLDERS:
    folders.remove(sorting_folder)

print(files)
print(folders)

VALID_IMAGES_EXTENSIONS = ("png", "jpg", "jpeg", "mp4", "avif", "webp", "gif", "ico", "jfif")
VALID_FILES_EXTENSIONS = ("exe", "lnk")

for file in files:
    if(file.lower().endswith(VALID_IMAGES_EXTENSIONS)):
        print("Trying to move image " + DESKTOP_PATH + file )
        orig_file = file
        while(os.path.isfile(DESKTOP_PATH + "Images/" + file)):
            print(DESKTOP_PATH + "Images/" + file + " already exists!")
            print("Renaming...")
            file = "1" + file
        print("Moving...")
        shutil.move(DESKTOP_PATH + orig_file, DESKTOP_PATH + "Images/" + file)
    elif(file.lower().endswith(VALID_FILES_EXTENSIONS)):
        print("Trying to move program " + DESKTOP_PATH + file )
        print("Moving...")
        shutil.move(DESKTOP_PATH + file, DESKTOP_PATH + "Programs/" + file)
    else:
        print("Trying to move file " + DESKTOP_PATH + file )
        print("Moving...")
        shutil.move(DESKTOP_PATH + file, DESKTOP_PATH + "Files/" + file)
    print("----------------------------------------------")
    
for folder in folders:
    print("Trying to move file folder " + DESKTOP_PATH + folder )
    orig_folder = folder
    while(os.path.isdir(DESKTOP_PATH + "Files/" + folder)):
            print(DESKTOP_PATH + "Files/" + folder + " already exists!")
            print("Renaming...")
            folder = "1" + folder
    print("Moving...")
    shutil.move(DESKTOP_PATH + orig_folder, DESKTOP_PATH + "Files/" + folder)
