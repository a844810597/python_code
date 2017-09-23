class FileObject:
    def __init__(self, file_path, open_mode='r'):
        self.file = open(file_path, open_mode)
        
    def __del__(self):
        self.file.close()
