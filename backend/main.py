from fastapi import FastAPI, Request

from api.inference import router as inf_router

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from validations.limiter import limiter

from fastapi.responses import JSONResponse

# creating fast api app
app = FastAPI(
    title="VoiceGuard API",
    description="API for VoiceGuard to detect malicious media",
    version="1.0.0" 
)


# Attach limiter to app
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

#Custom 429 handler (THIS FIXES "Undocumented")
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "success": False,
            "error": "RATE_LIMIT_EXCEEDED",
            "message": "Too many requests. Please try again later."
        },
        headers={"Retry-After": "60"}
    )

# Import router AFTER limiter is defined
from api.inference import router as inference_router

app.include_router(inf_router, prefix="/api/v1")


