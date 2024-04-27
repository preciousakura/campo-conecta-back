from pydantic import BaseModel
from app.schemas.user import UserReturn

class AuthenticatedUser(BaseModel):
  access_token: str
  user: UserReturn