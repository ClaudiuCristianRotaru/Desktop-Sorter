from classes.SortedFolder import SortedFolder
class Config:
    default_folder: str
    excluded_files: list[str]
    sorting_folders: list[SortedFolder]
    