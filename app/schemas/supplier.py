from pydantic import BaseModel

class SupplierBase(BaseModel):
  name: str
  logo: str | None = None
  slogan: str | None = None
  description: str | None = None

class Supplier(SupplierBase):
  id: int
