from fastapi.responses import JSONResponse
from typing import Optional

def response(message: str, data: Optional[dict] = None, status: int = 200) -> JSONResponse:
    return JSONResponse(
        {'message': message, 'data': data if data is not None else {}}, 
        status_code=status
    )
