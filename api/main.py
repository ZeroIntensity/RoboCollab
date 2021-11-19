import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils import StateConfig, Config, render_routes
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from db import validate_auth


app = FastAPI()
render_routes(app)
ip = StateConfig["ip"]
port = StateConfig["port"]

@app.get('/')
def index():
    return Config["home_message"]

@app.middleware("http")
async def auth(request: Request, call_next):
    if StateConfig["require_auth"]:
        headers = request.headers
        if not "auth" in headers:
            return JSONResponse({
                "error": "Authentication is required.",
                "status": 403
            }, status_code = 403)
        
        token = headers["auth"]

        if not validate_auth(token):
            return JSONResponse({
                "error": "Invalid authentication token.",
                "status": 403
            }, status_code = 403)

    response = await call_next(request)
    return response



if Config["production"]:
    app.add_middleware(HTTPSRedirectMiddleware)

if __name__ == "__main__":
    uvicorn.run(app, host = ip, port = port)