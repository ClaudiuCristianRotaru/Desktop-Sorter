from classes.SortedFolder import SortedFolder
class Config:
    default_folder: str
    excluded_files: list[str]
    sorting_folders: list[SortedFolder]
    
    def __init__(self, default_folder: str, excluded_files: list[str], sorting_folders: list[SortedFolder]):
        self.default_folder: str = default_folder
        self.excluded_files: list[str] = excluded_files
        self.sorting_folders: list[SortedFolder] = sorting_folders