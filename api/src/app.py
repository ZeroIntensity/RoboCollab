import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from config import STATE_CONFIG, CONFIG
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from db import validate_auth
from .json_res import json_response
from .schema import schema

app = FastAPI()

@app.get('/')
def index():
    return json_response("Welcome to the RoboCollab API!")

@app.middleware("http")
async def auth(request: Request, call_next):
    if STATE_CONFIG["require_auth"]:
        headers = request.headers

        if not "auth" in headers:
            return json_response("Authentication is required.", 400)
        
        token = headers["auth"]

        if not validate_auth(token):
            return json_response("Invalid authentication token.", 403)

    response = await call_next(request)
    return response

if CONFIG["production"]:
    app.add_middleware(HTTPSRedirectMiddleware)

def run():
    uvicorn.run(app, host = ip, port = port) # type: ignore