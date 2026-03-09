import os
import shutil

class FileManager:
    def __init__(self, base_path=None):
        self.base_path = base_path if base_path else os.path.expanduser("~")

    def list_files(self, path=None):
        path = path if path else self.base_path
        try:
            items = os.listdir(path)
            return items
        except Exception as e:
            return [str(e)]

    def delete_file(self, filepath):
        full_path = os.path.join(self.base_path, filepath)
        if os.path.isfile(full_path):
            os.remove(full_path)
            return True
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
            return True
        return False
