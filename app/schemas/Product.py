from typing import Annotated
from pydantic import BaseModel, Field
from app.models import ProductType
from app.schemas.supplier import Supplier

class ProductBase(BaseModel):
  name: str
  supplier_id: int
  price: float
  total_available: int
  description: str | None = None
  size: str | None = None
  product_type: ProductType | None = None
  rating: Annotated[int, Field(le=5, ge=0)]
  picture: str = 'https://images.unsplash.com/photo-1603186741833-4a7cf699a8eb?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

class Product(ProductBase):
  id: int

class ProductUpdate(BaseModel):
  name: str | None = None
  supplier_id: int | None = None
  description: str | None = None
  price: float | None = None
  total_available: int | None = None
  size: str | None = None
  picture: str | None = None
  product_type: ProductType | None = None
  rating: Annotated[int | None, Field(le=5, ge=0)] = None

class ProductWithRelations(Product):
  supplier: list[Supplier]
