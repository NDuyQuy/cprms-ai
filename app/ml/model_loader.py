from sentence_transformers import SentenceTransformer
from app.core.config import settings

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(settings.MODEL_PATH,revision=settings.COMMIT_HASH,trust_remote_code=True)
    return _model