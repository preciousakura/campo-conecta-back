from fastapi import FastAPI
from fastapi.responses import JSONResponse

def error_500_handler(request, exc):
  return JSONResponse(status_code=500, content={ 'message': 'INTERNAL_SERVER_ERROR' })

def add_error_handlers(app: FastAPI):
  app.add_exception_handler(500, error_500_handler)
