import random

def run_model(file_bytes: bytes):
    confidence=round(random.uniform(0.5, 1.0), 2)
    is_fake= confidence > 0.75

    return {
        "is_fake": is_fake,
        "confidence": confidence,
        "model_version": "1.0.0"
    }

