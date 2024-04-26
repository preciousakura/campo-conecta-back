from fastapi import FastAPI
from app.routers import auth, product
from dotenv import load_dotenv
from app.errors import add_error_handlers
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

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
