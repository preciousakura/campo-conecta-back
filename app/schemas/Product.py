from pydantic import BaseModel

class BaseProduct(BaseModel):
  name: str
  price: float
  total_available: int
  description: str | None = None

class Product(BaseProduct):
  id: int
  picture: str | None = None
