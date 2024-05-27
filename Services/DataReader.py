import os


def read_image(filepath: str):
    if not os.path.exists(filepath):
        raise Exception("File doesn't exist")
    else:
        return {'vol': os.path.normpath(filepath)}
