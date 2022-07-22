import os

from settings import UPLOAD_PATH

async def file_upload(file):   #saves the uploaded file and returns filepath
    file_path = os.path.join(UPLOAD_PATH, file.filename)
    with open(file_path, "wb+") as file_object:
        file_object.write(file.file.read())
    return file_path
