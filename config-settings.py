from classes.SortedFolder import SortedFolder
from classes.ConfigManager import ConfigManager
import os


def clear_console():
    os.system("cls")


def print_sorting_folders(sorting_folders: list[SortedFolder]) -> None:
    print("Current sorting folders are: ")
    for folder in sorting_folders:
        print(folder.name, "containing", folder.associated_types, "type files")
    print("\nReminder: '*' type = folders\n")


def print_menu_options() -> None:
    print("""
------------MENU------------------------
    Options: 
        1. Display current config
        2. Add a new sorting folder
        3. Remove a sorting folder
        4. Clear all folders
        0. Exit
----------------------------------------""")


def create_sorting_folder() -> SortedFolder:
    name: str = input("Folder name: ")
    types: str = input("Folder associated types(separate by spaces): ")
    types_array = types.split(" ")
    return SortedFolder(name, types_array)


def main() -> None:
    config_manager: ConfigManager = ConfigManager
    json_data_string = config_manager.load_config_from_file("./config.json")
    sorting_folders: list[SortedFolder] = config_manager.deserialize_config_json(
        json_data_string
    )

    config_manager: ConfigManager = ConfigManager

    isRunning: bool = True
    while isRunning:
        print_menu_options()

        try:
            option = int(input("Enter your option: "))
        except:
            option = 9
        clear_console()
        match option:
            case 1:
                print_sorting_folders(sorting_folders)
            case 2:
                sorted_folder = create_sorting_folder()
                sorting_folders.append(sorted_folder)
                config_manager.save_config_to_file("./config.json", sorting_folders)
                print("Created folder", sorted_folder.name)
            case 3:
                folder_name = input("Input folder name to be removed: ")
                for folder in sorting_folders:
                    if folder_name == folder.name:
                        sorting_folders.remove(folder)
                        print("Removed folder", folder.name)
                        break
                config_manager.save_config_to_file("./config.json", sorting_folders)
            case 4:
                config_manager.save_config_to_file("./config.json", [])
                print("Removed all folders")
            case 0:
                isRunning = False
                print("Stopping...")
            case _:
                print("Not a valid option")


if __name__ == "__main__":
    main()
