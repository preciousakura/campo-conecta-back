from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
  email: str
  name: str
  last_name: str

  model_config = ConfigDict({
    'from_attributes': True
  })

class UserReturn(UserBase):
  id: int

class UserCreate(UserBase):
  password: str
