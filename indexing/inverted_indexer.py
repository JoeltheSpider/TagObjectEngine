from ..retrieval.fs_utils import FileSystemUtils

class InvertedIndexer:

    def load_store():
        pass

    def dump_store():
        pass

    def create_store(self, file_paths):
        #iterate through file_paths and create index
        for file_path in file_paths:
            content = FileSystemUtils.load_file(file_path)
            # hash
            # check if hash exists, compare file
            # if same then add file path to object meta
            # else create new object meta and store (index, hash, file_path) sqlite db

    def index_object(self, _object, tag):
        # index: (tag -> object_meta_index)
        # approach: create new index for each tag
        pass

    def get_filenames(self, tag):
        # refer inverted index and return all filenames
        pass

    def get_all_filenames(self):
        #iterate through and get all filenames in sqlite db
        pass