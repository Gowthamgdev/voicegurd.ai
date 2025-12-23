from fastapi import FastAPI
from api.inference import router as inf_router

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from validations.limiter import limiter

# creating fast api app
app = FastAPI(
    title="VoiceGuard API",
    description="API for VoiceGuard to detect malicious media",
    version="1.0.0" 
)


# Attach limiter to app
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Handle rate limit errors
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Import router AFTER limiter is defined
from api.inference import router as inference_router

app.include_router(inf_router, prefix="/api/v1")


