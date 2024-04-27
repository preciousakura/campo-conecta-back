from app.schemas.product import Product
from datetime import datetime, date
from pydantic import BaseModel

class OrderCreate(BaseModel):
  amount: int
  product_id: int
  delivery_price: float

class Order(BaseModel):
  id: int
  amount: int
  price: float
  user_id: int
  product_id: int
  delivery_price: float
  delivery_time: date
  created_at: datetime
  updated_at: datetime

class OrderWithRelations(Order):
  product: Product
