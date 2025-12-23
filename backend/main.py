from fastapi import FastAPI
from api.inference import router as inf_router


app = FastAPI(
    title="VoiceGuard API",
    description="API for VoiceGuard to detect malicious media",
    version="1.0.0" 
)

app.include_router(inf_router, prefix="/api/v1")


