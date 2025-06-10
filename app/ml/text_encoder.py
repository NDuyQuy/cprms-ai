from app.ml.model_loader import get_model
import json

# trả về list json là kết quả encode của text từng field
def encode_fields(field_texts: dict) -> dict: #encode list field gửi từ .net
    model = get_model()
    result = {}
    for field_name, text in field_texts.items():
        embedding = model.encode(text)
        result[field_name] = json.dumps(embedding.tolist())
    return result