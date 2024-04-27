from typing import Annotated
from pydantic import BaseModel, Field
from app.models import ProductType
from app.schemas.supplier import Supplier
from datetime import date

class ProductBase(BaseModel):
  name: str
  supplier_id: int
  price: float
  description: str | None = None
  size: str | None = None
  product_type: ProductType | None = None
  rating: Annotated[int, Field(le=5, ge=0)]

  total_orders: int | None = None
  min_orders: int  | None = None
  total_selled: float  | None = None
  delivery_price: float  | None = None
  delivery_time: date  | None = None
  picture: str = 'https://images.unsplash.com/photo-1603186741833-4a7cf699a8eb?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

class Product(ProductBase):
  id: int

class ProductUpdate(BaseModel):
  name: str | None = None
  supplier_id: int | None = None
  description: str | None = None
  price: float | None = None
  size: str | None = None
  picture: str | None = None
  product_type: ProductType | None = None
  rating: Annotated[int | None, Field(le=5, ge=0)] = None
  delivery_price: float | None = None
  delivery_time: date | None = None

class ProductWithRelations(Product):
  supplier: list[Supplier]
