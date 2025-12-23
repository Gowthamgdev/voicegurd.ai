from fastapi import UploadFile, HTTPException


allowed_file_types = ["audio/mpeg", "audio/wav", "video/mp4", "video/mkv", "audio/x-m4a"]

max_file_size_mb = 50

def validate_file_type(file: UploadFile):
    if file.content_type not in allowed_file_types:
        raise HTTPException(
            status_code=400,
            detail="Unsupported media type."
        )
    
    file.file.seek(0,2)
    size=file.file.tell()
    file.file.seek(0)
    if size > max_file_size_mb * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds the maximum limit."
        )