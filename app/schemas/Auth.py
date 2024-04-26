from pydantic import BaseModel
from app.schemas.User import UserReturn

class AuthenticatedUser(BaseModel):
  access_token: str
  user: UserReturn