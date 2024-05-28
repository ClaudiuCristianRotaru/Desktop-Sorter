from classes.SortedFolder import SortedFolder
import json


class ConfigManager:
    def load_config_from_file(path: str) -> str:
        with open(path, "r") as file:
            return file.read()

    def deserialize_config_json(json_data_string: str) -> list[SortedFolder]:
        json_data_dict = json.loads(json_data_string)
        sorted_folders: list[SortedFolder] = []
        for folder in json_data_dict:
            dir: SortedFolder = SortedFolder("", [])

            dir.name = folder["name"]

            associated_types = folder["associated_types"]
            for type in associated_types:
                dir.associated_types.append(type)

            sorted_folders.append(dir)
        return sorted_folders

    def save_config_to_file(path: str, sorted_folders: list[SortedFolder]) -> None:
        with open(path, "w") as file:
            file.write("[")
            i: int
            for i in range(len(sorted_folders) - 1):
                file.write(sorted_folders[i].to_json())
                file.write(",\n")
            file.write(sorted_folders[i + 1].to_json())
            file.write("]")
