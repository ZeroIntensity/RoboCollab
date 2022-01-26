from fastapi.responses import JSONResponse
from typing import Any

def json_response(message: Any, status: int = 200, key_name: str = 'message') -> JSONResponse:
    return JSONResponse({key_name: message, status: status}, status_code = status)