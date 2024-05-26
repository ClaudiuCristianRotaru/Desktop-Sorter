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
    
    def serialize_config_json(sorted_folders:list[SortedFolder])-> None:
        res = json.dumps(sorted_folders)
        print(res)