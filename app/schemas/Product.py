from pydantic import BaseModel

class BaseProduct(BaseModel):
  name: str
  price: float
  total_available: int
  description: str | None = None

class Product(BaseProduct):
  id: int
  picture: str | None = None

class ProductUpdate(BaseModel):
  name: str | None = None
  price: float | None = None
  total_available: int | None = None
  description: str | None = None
  picture: str | None = None
