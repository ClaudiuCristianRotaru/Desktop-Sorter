from classes.SortedFolder import SortedFolder
from classes.ConfigManager import ConfigManager
import os


def clear_console():
    os.system("cls")


def print_sorting_folders(sorting_folders: list[SortedFolder]) -> None:
    print("Current sorting folders are: ")
    for folder in sorting_folders:
        print(folder.name, "containing", folder.associated_types, "type files")
    print("\nReminder: '*' type = folders")


def main() -> None:
    config_manager: ConfigManager = ConfigManager
    json_data_string = config_manager.load_config_from_file("./config.json")
    sorting_folders: list[SortedFolder] = config_manager.deserialize_config_json(
        json_data_string
    )
    print_sorting_folders(sorting_folders)


if __name__ == "__main__":
    main()
