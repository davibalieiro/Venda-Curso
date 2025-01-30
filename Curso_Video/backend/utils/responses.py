from fastapi.responses import JSONResponse

def response(message: str, data=None, status=200):
    return JSONResponse({'message': message, 'data': data}, status_code=status)