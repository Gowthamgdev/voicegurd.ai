from fastapi import APIRouter, UploadFile, File, Request
from validations.validators import validate_file_type
from services.model import run_model
from schemas.response import DetectionResponse, RateLimitError
from validations.limiter import limiter




router = APIRouter()


@router.post("/detect", 
             response_model=DetectionResponse,responses={
        429: {
            "model": RateLimitError,
            "description": "Rate limit exceeded"
        }
    })
@limiter.limit("5/minute")
async def detect_media(request: Request,file: UploadFile = File(...)):

    validate_file_type(file)
    
    file_bytes = await file.read()
    result=run_model(file_bytes)

    return DetectionResponse(
        success=True,
        file_name=file.filename,
        media_type=file.content_type,
        is_fake=result["is_fake"],
        confidence=result["confidence"],
        model_version=result["model_version"],
        message="Detection completed successfully."
    )



