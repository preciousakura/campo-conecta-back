from sqlalchemy.orm import Session
from app.schemas.User import UserCreate
from app import models
import bcrypt
import os
import jwt

def signup(db: Session, user: UserCreate):
  user.password = bcrypt.hashpw(str.encode(user.password), bcrypt.gensalt(10)).decode()
  db_user = models.User(**user.model_dump())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  
  access_token = jwt.encode({ 'id': db_user.id }, os.getenv("JWT_KEY"))

  return {
    'user': db_user,
    'access_token': access_token
  }
