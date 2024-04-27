from app.schemas.product import Product
from datetime import datetime, date
from pydantic import BaseModel

class OrderCreate(BaseModel):
  amount: int
  product_id: int

class Order(BaseModel):
  id: int
  amount: int
  user_id: int
  product_id: int
  created_at: datetime
  updated_at: datetime

class OrderWithRelations(Order):
  product: Product
