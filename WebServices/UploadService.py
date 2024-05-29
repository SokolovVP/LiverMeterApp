import os
from glob import glob


class UploadService:

    @staticmethod
    def upload_file(file, file_dir):
        _filename = file.filename

        file.save(os.path.normpath(os.path.join(file_dir, _filename)))

        return _filename
