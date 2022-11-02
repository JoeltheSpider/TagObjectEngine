from ..logger import logger
import os
from .. import config

# filesystem related utilities (static) 
class FileSystemUtils:
    
    def fetch_all_files(root_folder):
        # get all file names from a given folder and its subfolders (!TODO: and its associated hash)
        folders = [root_folder] # stack logic
        while len(folders):
            folder_path = folders.pop(0)
            for filename in os.listdir(folder_path):
                entity = folder_path + "//" + filename
                if os.path.isfile(entity):
                    yield entity
                else:
                    folders.append(entity)
                    logger.info("Adding to queue: ", filename, "in", folder_path)

    def fetch_files(folder_path):
        # get all file names from a given folder (!TODO: and its associated hash)
        for filename in os.listdir(folder_path):
            entity = folder_path + "//" + filename
            if os.path.isfile(entity):
                yield entity
            else:
                logger.info("Skipping", filename, "in", folder_path)

    def load_file(file_path):
        # load a file from filesystem
        content = ""
        with open(file_path, "r") as file:
            content = file.read()
        return content