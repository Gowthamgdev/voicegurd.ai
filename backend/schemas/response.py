from pydantic import BaseModel

class DetectionResponse(BaseModel):
    sucess: bool
    file_name: str
    media_type: str
    is_fake: bool
    confidence: float
    model_version: str
    message: str
    