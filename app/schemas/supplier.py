from typing import Annotated
from pydantic import BaseModel, Field

class SupplierBase(BaseModel):
  name: str
  rating: Annotated[int, Field(le=5, ge=0)]
  logo: str | None = None
  slogan: str | None = None
  description: str | None = None

class Supplier(SupplierBase):
  id: int
