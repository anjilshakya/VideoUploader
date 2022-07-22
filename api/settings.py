import os

UPLOAD_PATH = 'files'
if not os.path.exists(UPLOAD_PATH):
    os.mkdir(UPLOAD_PATH)
