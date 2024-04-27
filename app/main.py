from fastapi import FastAPI
from app.routers import auth, product, order, populate
from dotenv import load_dotenv
from app.errors import add_error_handlers
from fastapi.middleware.cors import CORSMiddleware
import os

APP_ROOT = os.path.join(os.path.dirname(__file__))
ENV_PATH = os.path.join(APP_ROOT, '.env')

load_dotenv(ENV_PATH)

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
add_error_handlers(app)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(populate.router)
