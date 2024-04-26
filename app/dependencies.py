from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app import models
from app.database.connection import engine, SessionLocal
from datetime import datetime
import jwt
import os

models.Base.metadata.create_all(bind=engine)
oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

unauthorized_exception = HTTPException(
  status_code=401,
  detail="Invalid token",
  headers={"WWW-Authenticate": "Bearer"},
)

def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
  try:
    decoded_token = jwt.decode(token, os.getenv('JWT_KEY'), algorithms=["HS256"])
    if datetime.fromisoformat(decoded_token['expires_in']) < datetime.today():
      raise unauthorized_exception
    return decoded_token['id']
  except Exception:
    raise unauthorized_exception

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()