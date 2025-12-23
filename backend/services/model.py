import random
import bentoml


@bentoml.service(
        name="VoiceGuardai_inference_service",
        traffic={"timeout":30}
)

class Bento_model:

    @bentoml.api
    def predict(self, file_bytes: bytes)-> dict:
        
        confidence=round(random.uniform(0.5, 1.0), 2)

        return{
            "is_fake": confidence > 0.75,
            "confidence": confidence,
            "model_version": "Bentomodel-1.0.0"
        }
        

model= Bento_model()


def run_model(file_bytes: bytes):
    return model.predict(file_bytes)

