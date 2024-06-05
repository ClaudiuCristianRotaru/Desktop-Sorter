from classes.SortedFolder import SortedFolder
from classes.Config import Config
import json


class ConfigManager:
    def load_config_from_file(path: str) -> str:
        with open(path, "r") as file:
            return file.read()

    def deserialize_config_json(json_data_string: str) -> Config:
        json_data_dict = json.loads(json_data_string)

        default_folder = json_data_dict["default_folder"]
        excluded_files: list[str] = json_data_dict["excluded_files"]
        
        sorting_folders_dict = json_data_dict["sorting_folders"]
        sorted_folders: list[SortedFolder] = []
        for folder in sorting_folders_dict:
            name = folder["name"]
            associated_types = folder["associated_types"]
            sorted_folders.append(SortedFolder(name, associated_types))

        print(type(associated_types[0]))
        config: Config = Config(default_folder, excluded_files, sorted_folders)
        return config

    def save_config_to_file(path: str, config: Config) -> None:
        with open(path, "w") as file:
            file.write(json.dumps(config.__dict__, indent=4))
