from fastapi.responses import JSONResponse

error = 404

def handler(request, exc):
    return JSONResponse({
        "message": "Not Found",
        "status": 404,
    }, status_code = 404)