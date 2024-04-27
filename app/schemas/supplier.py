from typing import Annotated
from pydantic import BaseModel, Field
from app.models import ProductType

class SupplierBase(BaseModel):
  name: str
  rating: Annotated[int, Field(le=5, ge=0)]
  logo: str | None = None
  slogan: str | None = None
  description: str | None = None

class Supplier(SupplierBase):
  id: int

class SupplierProduct(BaseModel):
  id: int
  name: str
  supplier_id: int
  price: float
  total_available: int
  description: str | None = None
  size: str | None = None
  product_type: ProductType | None = None
  rating: Annotated[int, Field(le=5, ge=0)]
  picture: str = 'https://images.unsplash.com/photo-1603186741833-4a7cf699a8eb?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

class SupplierWithRelations(Supplier):
  products: list[SupplierProduct]

class MostSelledProductInfo(BaseModel):
  supplier_id: int
  id: int
  name: str
  rating: int
  picture: str
  price: float
  total_sells: int

class SupplierInfo(BaseModel):
  supplier: SupplierWithRelations
  most_selled_items: list[MostSelledProductInfo]