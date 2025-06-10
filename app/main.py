from fastapi import FastAPI
from .api.endpoint  import encode_fields
from .api.endpoint import compare_project
app = FastAPI()

app.include_router(encode_fields.router, prefix="/api")
app.include_router(compare_project.router, prefix="/api")