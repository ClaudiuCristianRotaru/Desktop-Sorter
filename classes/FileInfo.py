class FileInfo:
    def __init__(self, name: str, extension: str, is_folder: bool):
        self.name: str = name
        self.extension: str = extension
        self.is_folder: bool = is_folder

    def get_full_name(self) -> str:
        if self.is_folder:
            return self.name
        else:
            return self.name + self.extension

    def get_extension(self) -> str:
        if self.is_folder:
            return ""
        else:
            return self.extension
