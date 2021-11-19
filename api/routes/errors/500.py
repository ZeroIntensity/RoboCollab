from fastapi.responses import JSONResponse

error = 404

def handler(request, exc):
    return JSONResponse({
        "message": "Internal Server Error",
        "status": 500,
    }, status_code = 500)