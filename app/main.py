from fastapi import FastAPI
from .api.endpoint  import encode_fields
from .api.endpoint import compare_project
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

# add middleware cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


app.include_router(encode_fields.router, prefix="/api")
app.include_router(compare_project.router, prefix="/api")