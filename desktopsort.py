import os
from os import walk
import shutil

class SortedFolder:
    def __init__(self, name, associated_types):
        self.name = name
        self.associated_types = associated_types

class FileInfo:
    def __init__(self, name, extension, is_folder):
        self.name = name
        self.extension = extension
        self.is_folder = is_folder

    def get_full_name(self):
        if(self.is_folder):
            return self.name
        else:
            return self.name+self.extension

def get_sorted_folders():
    sorted_folders = []
    sorted_folders.append(SortedFolder("Games", [".exe"]))
    sorted_folders.append(SortedFolder("Files", [".txt", ".pdf", ".html", "*"]))
    sorted_folders.append(SortedFolder("Images", [".png", ".jpg", ".webp", ""]))
    return sorted_folders

def get_sorting_files(path):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
        for file_name in filenames:
            extension_index = file_name.rfind('.')
            if ( extension_index != -1):
                file = FileInfo(file_name[0:extension_index],file_name[extension_index:], False)
            else:
                file = FileInfo(file_name, '', False)
            files.append(file)
        for dir_name in dirnames:
            file = FileInfo(dir_name, "*", True)
            files.append(file)
        break
    return files

def exclude_sorting_files(files, excluded_files):
    new_files = []
    for file in files:
        found = False
        for excluded_file in excluded_files:
            if(excluded_file.name == file.name):
                found = True
        if (found == False):
            new_files.append(file)
    return new_files
    

def create_output_folders(path, folders):
    for folder in folders:
        if (not os.path.isdir(path + "\\" + folder.name)):
            print(f"Creating folder {folder.name}")
            os.mkdir(path+"\\"+folder.name)
    print()

def move_file(path, file, folder):
    print(f"Trying to move '{file.get_full_name()}' to '{folder.name}'...\n")
    shutil.move(path + '\\' + file.get_full_name(), path + "\\" + folder.name + '\\' + file.get_full_name())

def sort_files(path, files, folders):
    for file in files:
        found = False
        for folder in folders:
            if file.extension in folder.associated_types:
                found = True
                move_file(path ,file, folder)
                break
        if(found == False):        
            print("No suitable folder found for", file.name, "of type", file.extension)
            
  
def main(): 
    # path = desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + '\\'
    path = '..\\ExampleDesktop'
    output_folders = get_sorted_folders()
    input_files = get_sorting_files(path)
    create_output_folders(path, output_folders)
    input_files = exclude_sorting_files(input_files,output_folders)
    sort_files(path, input_files, output_folders)
  
if __name__=="__main__": 
    main() 






# # Get desktop path (tested only for Windows)
# DESKTOP_PATH = desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + '\\'
# # Don't try to move these files
# NONO_FILES = ["desktop.ini", "SortDesktop.lnk"]
# SORTING_FOLDERS = ["Games", "Images", "Programs", "Files"]
# folders = []
# files = []
# for (dirpath, dirnames, filenames) in walk(DESKTOP_PATH):
#     files.extend(filenames)
#     folders.extend(dirnames)
#     break

# for nono_file in NONO_FILES:
#     files.remove(nono_file)

# for sorting_folder in SORTING_FOLDERS:
#     folders.remove(sorting_folder)

# print(files)
# print(folders)

# VALID_IMAGES_EXTENSIONS = ("png", "jpg", "jpeg", "mp4", "avif", "webp", "gif", "ico", "jfif")
# VALID_FILES_EXTENSIONS = ("exe", "lnk")

# for file in files:
#     if(file.lower().endswith(VALID_IMAGES_EXTENSIONS)):
#         print("Trying to move image " + DESKTOP_PATH + file )
#         orig_file = file
#         while(os.path.isfile(DESKTOP_PATH + "Images/" + file)):
#             print(DESKTOP_PATH + "Images/" + file + " already exists!")
#             print("Renaming...")
#             file = "1" + file
#         print("Moving...")
#         shutil.move(DESKTOP_PATH + orig_file, DESKTOP_PATH + "Images/" + file)
#     elif(file.lower().endswith(VALID_FILES_EXTENSIONS)):
#         print("Trying to move program " + DESKTOP_PATH + file )
#         print("Moving...")
#         shutil.move(DESKTOP_PATH + file, DESKTOP_PATH + "Programs/" + file)
#     else:
#         print("Trying to move file " + DESKTOP_PATH + file )
#         print("Moving...")
#         shutil.move(DESKTOP_PATH + file, DESKTOP_PATH + "Files/" + file)
#     print("----------------------------------------------")
    
# for folder in folders:
#     print("Trying to move file folder " + DESKTOP_PATH + folder )
#     orig_folder = folder
#     while(os.path.isdir(DESKTOP_PATH + "Files/" + folder)):
#             print(DESKTOP_PATH + "Files/" + folder + " already exists!")
#             print("Renaming...")
#             folder = "1" + folder
#     print("Moving...")
#     shutil.move(DESKTOP_PATH + orig_folder, DESKTOP_PATH + "Files/" + folder)
