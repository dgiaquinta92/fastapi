from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse, JSONResponse, RedirectResponse
from starlette.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import io
import requests
import urllib3
urllib3.disable_warnings()

from security import security
from procedures import procedures
from modelos import modelos as md
from routers import router_v1
from logs import logs_middleware


app = FastAPI()


tags_metadata = [
    {
        "name": "DRINKS",
        "description": "Request de Obtención de CSV DRINKS",
        "externalDocs": {
            "description": "Link",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "TEST",
        "description": "Request de prueba",
        "externalDocs": {
            "description": "Link a Dashboard o algo",
            "url": "https://fastapi.tiangolo.com/",
        },
    }    
]
description = "API de Prueba"



app = FastAPI(title="API - PyDay2023", version="1.0", 
              description = description, openapi_tags=tags_metadata)

app.include_router(router_v1.router, prefix="/api/v1")

app.add_middleware(CORSMiddleware, allow_origins=["*"], 
                   allow_credentials=True, allow_methods=["*"], 
                   allow_headers=["*"])
app.add_middleware(logs_middleware.RequestLoggingMiddleware)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


