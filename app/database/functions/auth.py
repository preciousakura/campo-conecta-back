from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app import models
from datetime import datetime, timedelta
import bcrypt
import os
import jwt

def signup(db: Session, user: UserCreate):
  user.password = bcrypt.hashpw(str.encode(user.password), bcrypt.gensalt(10)).decode()
  db_user = models.User(**user.model_dump())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  
  expires_in = datetime.today() + timedelta(days=15)
  access_token = jwt.encode({ 'id': db_user.id, 'expires_in': expires_in.isoformat() }, os.getenv('JWT_KEY'))

  return {
    'user': db_user,
    'access_token': access_token
  }

def signin(db: Session, email: str, password: str):
  user = db.query(models.User).filter(models.User.email == email).first()

  if user is None:
    raise HTTPException(500)
  
  user_password = user.password.encode()
  if bcrypt.checkpw(password.encode(), user_password):
    expires_in = datetime.today() + timedelta(days=15)
    access_token = jwt.encode({ 'id': user.id, 'expires_in': expires_in.isoformat() }, os.getenv('JWT_KEY'))
    return {
      'access_token': access_token,
      'user': user
    }
  else:
    raise HTTPException(500)
  
def verify(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()
