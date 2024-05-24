import os
from os import walk
import shutil
import classes.FileInfo as FileInfo
import classes.SortedFolder as SortedFolder

def get_sort_output_folders():
    sorted_folders = []
    sorted_folders.append(SortedFolder("Games", [".exe"]))
    sorted_folders.append(SortedFolder("Files", [".txt", ".pdf", ".html", "*"]))
    sorted_folders.append(SortedFolder("Images", [".png", ".jpg", ".webp", ""]))
    return sorted_folders

def get_sorting_files(path):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
        for file_name in filenames:
            extension_index = file_name.rfind(".")
            if ( extension_index != -1):
                file = FileInfo(file_name[0:extension_index],file_name[extension_index:], False)
            else:
                file = FileInfo(file_name, "", False)
            files.append(file)
        for dir_name in dirnames:
            file = FileInfo(dir_name, "*", True)
            files.append(file)
        break
    return files

def exclude_sorting_files(files, excluded_files):
    accepted_files = []
    for file in files:
        found = False
        for excluded_file in excluded_files:
            if(excluded_file.name == file.name):
                found = True
        if not found:
            accepted_files.append(file)
    return accepted_files
    

def create_output_folders(path, folders: SortedFolder):
    for folder in folders:
        if (not os.path.isdir(f"{path}\\{folder.name}")):
            print(f"Creating folder '{folder.name}'")
            os.mkdir(f"{path}\\{folder.name}")
    print()
    
def isFileDuplicate(full_path, is_folder):
    if is_folder:
        return os.path.isdir(full_path)
    else:
        return os.path.isfile(full_path)
    
def generate_unique_name(path,file,folder):
    new_name = file.name
    index = 1
    while isFileDuplicate(f"{path}\\{folder.name}\\{new_name}{file.get_extension()}",file.is_folder):
        print(f"'{folder.name}\\{new_name}' already exists!")
        print("Renaming...")
        new_name = file.name + str(index)
        index += 1
    if(new_name!=file.name):
        print(f"Renamed '{file.get_full_name()}' to '{new_name}{file.get_extension()}'")
    return new_name

def move_file(path, file, folder):
    print(f"Trying to move '{file.get_full_name()}' to '{folder.name}'...\n")
    new_name = generate_unique_name(path,file,folder)
    shutil.move(f"{path}\\{file.get_full_name()}", f"{path}\\{folder.name}\\{new_name}{file.get_extension()}")

def sort_files(path, files, folders):
    for file in files:
        found = False
        for folder in folders:
            if file.extension in folder.associated_types:
                found = True
                move_file(path ,file, folder)
                break
        if not found:        
            print(f"No suitable folder found for '{file.name}' of type {file.extension}")
            
  
def main(): 
    # path = desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + '\\'
    path = "..\\ExampleDesktop"
    output_folders = get_sort_output_folders()
    input_files = get_sorting_files(path)
    create_output_folders(path, output_folders)
    input_files = exclude_sorting_files(input_files,output_folders)
    sort_files(path, input_files, output_folders)
  
if __name__=="__main__": 
    main() 