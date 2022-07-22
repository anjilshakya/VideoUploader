'''This file contains the schema for api's request'''

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel , Field

class ChargesInput(BaseModel): #schema for charge_list api for user request
    video_size : int
    length : int
    types : str
