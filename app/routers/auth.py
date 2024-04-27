from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies import get_db, get_current_user
from app.schemas.user import UserCreate
from app.schemas.auth import AuthenticatedUser
from app.database.functions import auth

router = APIRouter(
  prefix='/auth',
  tags=['auth']
)

@router.post('/signup', status_code=200, response_model=AuthenticatedUser)
def signup(db: Annotated[Session, Depends(get_db)], user: UserCreate):
  return auth.signup(db, user)

@router.post('/signin', status_code=200, response_model=AuthenticatedUser)
def signin(db: Annotated[Session, Depends(get_db)], form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
  return auth.signin(db, form_data.username, form_data.password)

@router.post('/verify', status_code=200)
def verify(user_id: Annotated[int, Depends(get_current_user)]):
  return user_id