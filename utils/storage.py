import os

def get_storage_path():
    try:
        from android.storage import primary_external_storage_path
        return primary_external_storage_path()
    except:
        return os.path.expanduser("~")
