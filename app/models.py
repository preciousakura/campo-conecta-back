from sqlalchemy import Column, String, Integer, Float, Text, Enum, DateTime, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from app.database.connection import Base
import enum

class ProductType(enum.Enum):
  PACKAGING = 'PACKAGING'
  SUPPLIE = 'SUPPLIE'
  EQUIPMENT = 'EQUIPMENT'
  LABEL = 'LABEL'
  OTHER = 'OTHER'

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  email = Column(String, unique=True, index=True, nullable=False)
  password = Column(String, nullable=False)
  name = Column(String, nullable=False)
  last_name = Column(String)

  orders = relationship('Order', back_populates='user')

class Product(Base):
  __tablename__ = 'product'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(Text)
  price = Column(Float, nullable=False)
  size = Column(String)
  picture = Column(String)
  product_type = Column(Enum(ProductType))
  rating = Column(Integer, nullable=False)

  total_orders = Column(Integer, nullable=False, default=0)
  min_orders = Column(Integer, nullable=False, default=1000)
  total_selled = Column(Float, nullable=False, default=0)
  delivery_price = Column(Float, nullable=None, default=50)
  delivery_time = Column(Date, default=expression.func.current_date() + expression.text("INTERVAL '10 days'"))

  orders = relationship('Order', back_populates='product')

  supplier_id = Column(Integer, ForeignKey('supplier.id'))
  supplier = relationship('Supplier', back_populates='products')

class Order(Base):
  __tablename__ = 'order'

  id = Column(Integer, primary_key=True)
  amount = Column(Integer, nullable=None)
  created_at = Column(DateTime, default=func.now())
  updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship('User', back_populates='orders')

  product_id = Column(Integer, ForeignKey('product.id'))
  product = relationship('Product', back_populates='orders')

class Supplier(Base):
  __tablename__ = 'supplier'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  rating = Column(Integer, nullable=False)
  logo = Column(String)
  slogan = Column(String)
  description = Column(String)

  products = relationship('Product', back_populates='supplier')