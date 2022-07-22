import os
import uvicorn

from fastapi import FastAPI, UploadFile, Form
from fastapi.encoders import jsonable_encoder

from upload_views import file_upload
from validators import file_validation, get_size
from settings import UPLOAD_PATH
from schema import ChargesInput, VideoSize

app = FastAPI()

app.mount("/static", StaticFiles(directory="files/"), name="static") #mount all the static files

@app.post("/upload-video/")
''' This api uploads video with less than 1 gb file size, having
    less than 10 minute of duration, supporting only .mp4 and .mkv '''
async def upload_video(file: UploadFile):
    file_path = await file_upload(file)
    validation_status, message = await file_validation(file, file_path)
    if validation_status:
        response = jsonable_encoder({"msg": "file uploaded successfully"})
    else:
        os.remove(file_path)
        response = jsonable_encoder({"msg": message})
    return response


@app.get("/list-video/")
''' This api lists all the uploaded videos '''
async def list_video():
    videos = os.listdir(UPLOAD_PATH)
    response = jsonable_encoder({"videos": videos})
    return response

@app.post("/charges-list/")
''' This api responds with the charge as per the user specification of uploading video '''
async def upload_charge(Inputs: ChargesInput):
    if Inputs.video_size < 500 and Inputs.length < 6.18:
        return {"msg":"It costs you 17.5$"}
    elif Inputs.video_size > 500 and Inputs.length <6.18:
        return {"msg":"It costs you 25$"}
    elif Inputs.video_size < 500 and Inputs.length > 6.18:
        return {"msg":"It costs you 25$"}
    elif Inputs.video_size > 500 and Inputs.length > 6.18:
        return {"msg":"It costs you 32.5$"}     

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
