from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.dependencies import get_db
from app.schemas.User import UserCreate
from app.database.functions import auth
from app.schemas.Auth import AuthenticatedUser

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

@router.post("/signup", response_model=AuthenticatedUser)
def signup(db: Annotated[Session, Depends(get_db)], user: UserCreate):
  return auth.signup(db, user)