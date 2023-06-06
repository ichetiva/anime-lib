from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


async def http_exception_handler(r: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content={"status": "error", "data": exc.detail}
    )
