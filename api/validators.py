'''This file contains the validators for api's'''

import cv2


async def file_validation(file, file_path): #checks the user file specification to upload the file
    message = "Success"
    status = True
    size = await get_size(file)
    duration = get_duration(file_path)
    if size > 1024:
        status = False
        message = "Too large file"
    if duration > 10:
        status = False
        message = "Too large duration"
    if not file.filename.endswith((".mp4", '.mkv')):
        status = False
        message = "Not supported extension"
    return status, message


def get_duration(filename): #returns the duration of file
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = (frame_count / fps) / 60
    return duration


async def get_size(file):
    return len(file.file.read()) * 0.000001

