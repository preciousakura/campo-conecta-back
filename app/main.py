from fastapi import FastAPI
from app.routers import auth
from dotenv import load_dotenv
from app.errors import add_error_handlers

load_dotenv()

app = FastAPI()
add_error_handlers(app)
app.include_router(auth.router)
