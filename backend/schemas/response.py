from pydantic import BaseModel

class DetectionResponse(BaseModel):
    success: bool
    file_name: str
    media_type: str
    is_fake: bool
    confidence: float
    model_version: str
    message: str

class RateLimitError(BaseModel):
    success: bool
    error: str
    message: str

class ValidationErrorResponse(BaseModel):
    detail: str