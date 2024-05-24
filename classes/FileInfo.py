class FileInfo:
    def __init__(self, name, extension, is_folder):
        self.name = name
        self.extension = extension
        self.is_folder = is_folder

    def get_full_name(self):
        if(self.is_folder):
            return self.name
        else:
            return self.name+self.extension
    
    def get_extension(self):
        if(self.is_folder):
            return ""
        else:
            return self.extension
