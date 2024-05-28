import os
from os import walk
import shutil
from classes.FileInfo import FileInfo
from classes.SortedFolder import SortedFolder
from classes.ConfigManager import ConfigManager
from dataclasses import asdict

def get_sorting_input_files(path: str) -> list[FileInfo]:
    input_files: list[FileInfo] = []
    for dirpath, dirnames, filenames in walk(path):
        for file_full_name in filenames:
            extension_index: int = file_full_name.rfind(".")
            if extension_index != -1:
                file_name: str = file_full_name[0:extension_index]
                file_extension: str = file_full_name[extension_index:]
                file = FileInfo(file_name, file_extension, False)
            else:
                file = FileInfo(file_full_name, "", False)
            input_files.append(file)

        for dir_name in dirnames:
            file = FileInfo(dir_name, "*", True)
            input_files.append(file)
        break
    return input_files


def exclude_sorting_files(
    files: FileInfo, excluded_files: FileInfo | SortedFolder
) -> list[FileInfo]:
    accepted_files: list[FileInfo] = []
    file: FileInfo
    for file in files:
        found: bool = False
        for excluded_file in excluded_files:
            if excluded_file.name == file.get_full_name():
                found = True
        if not found:
            accepted_files.append(file)
    return accepted_files


def create_output_folders(path: str, folders: list[SortedFolder]) -> None:
    for folder in folders:
        if not os.path.isdir(f"{path}\\{folder.name}"):
            print(f"Creating folder '{folder.name}'")
            os.mkdir(f"{path}\\{folder.name}")
    print()


def doesFileExist(full_path: str) -> bool:
    return os.path.isdir(full_path) or os.path.isfile(full_path)


def generate_unique_name(path: str, file: FileInfo, folder: SortedFolder) -> str:
    new_name: str = file.name
    index: int = 1
    while (
        doesFileExist(f"{path}\\{folder.name}\\{new_name}{file.get_extension()}")
        is True
    ):
        print(f"'{folder.name}\\{new_name}' already exists!")
        print("Renaming...")
        new_name = file.name + str(index)
        index += 1
    if new_name != file.name:
        print(f"Renamed '{file.get_full_name()}' to '{new_name}{file.get_extension()}'")
    print("-------------------------\n")
    return new_name


def move_file(path: str, file: FileInfo, folder: SortedFolder) -> None:
    print(f"Trying to move '{file.get_full_name()}' to '{folder.name}'...\n")
    new_name: str = generate_unique_name(path, file, folder)
    shutil.move(
        f"{path}\\{file.get_full_name()}",
        f"{path}\\{folder.name}\\{new_name}{file.get_extension()}",
    )


def sort_files(path: str, files: list[FileInfo], folders: list[SortedFolder]) -> None:
    for file in files:
        found: bool = False
        for folder in folders:
            if file.extension in folder.associated_types:
                found = True
                move_file(path, file, folder)
                break
        if not found:
            print(
                f"No suitable folder found for '{file.name}' of type {file.extension}"
            )
            print("-------------------------\n")


def main() -> None:
    # path = desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + '\\'
    path: str = "..\\ExampleDesktop"

    output_folders: list[SortedFolder] = []
    config_manager: ConfigManager = ConfigManager
    json_data_string = config_manager.load_config_from_file("./config.json")
    output_folders = config_manager.deserialize_config_json(json_data_string)
    create_output_folders(path, output_folders)

    input_files: FileInfo = []
    input_files = get_sorting_input_files(path)
    input_files = exclude_sorting_files(input_files, output_folders)
    
    sort_files(path, input_files, output_folders)
    
if __name__ == "__main__":
    main()
