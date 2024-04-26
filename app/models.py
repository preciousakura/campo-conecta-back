from sqlalchemy import Column, String, Integer, Float, Text, Enum
from app.database.connection import Base
import enum

class ProductType(enum.Enum):
  PACKAGING = 'PACKAGING'
  SUPPLIE = 'SUPPLIE'
  EQUIPMENT = 'EQUIPMENT'
  LABEL = 'LABEL'

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  email = Column(String, unique=True, index=True, nullable=False)
  password = Column(String, nullable=False)
  name = Column(String, nullable=False)
  last_name = Column(String)

class Product(Base):
  __tablename__ = 'product'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(Text)
  price = Column(Float, nullable=False)
  total_available = Column(Integer, nullable=False)
  picture = Column(String)
  product_type = Column(Enum(ProductType))
