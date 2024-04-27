from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from app.schemas.product import ProductBase
from app.schemas.supplier import SupplierBase
from app.schemas.utils import Order
from app import models
import math

def create(db: Session, product: ProductBase):
  db_product = models.Product(**product.model_dump())
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product

# apenas para teste
def update(db: Session, product_id: int, product: ProductBase):
  db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
  if db_product is None:
    raise HTTPException(404)
  
  for key, val in product.model_dump(exclude_unset=True).items():
    setattr(db_product, key, val)

  db.commit()
  db.refresh(db_product)
  return db_product

def index(db: Session, page: int, size: int, min_price: int | None, max_price: int | None, price_order: Order | None, search: str | None, available: bool | None, product_type: models.ProductType | None = None):
  items_query = db.query(models.Product)

  if min_price is not None:
    items_query = items_query.filter(models.Product.price >= min_price)

  if max_price is not None:
    items_query = items_query.filter(models.Product.price <= max_price)

  if search is not None:
    items_query = items_query.filter(models.Product.name.ilike(f'%{search}%'))

  if available:
    items_query = items_query.filter(models.Product.total_available > 0)

  if product_type is not None:
    items_query = items_query.filter(models.Product == product_type)

  total = items_query.with_entities(func.count(models.Product.id)).scalar()
  pages = math.ceil(total / size)

  if price_order == Order.ASC:
    items_query = items_query.order_by(models.Product.price.asc())
  elif price_order == Order.DESC:
    items_query = items_query.order_by(models.Product.price.desc())
  else:
    items_query = items_query.order_by(models.Product.id.asc())

  items = items_query.offset(page * size).limit(size).all()

  return {
    'items': items,
    'total': total,
    'pages': pages,
    'size': size,
    'page': page
  }

def delete(db: Session, product_id: int):
  db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
  if db_product is None:
    raise HTTPException(404)
  
  db.delete(db_product)
  db.commit()
  return { 'deleted': True }
  
def create_supplier(db: Session, new_supplier: SupplierBase):
  new_supplier = models.Supplier(**new_supplier.model_dump())
  db.add(new_supplier)
  db.commit()
  db.refresh(new_supplier)
  return new_supplier

def get_supplier_info(db: Session, supplier_id: int):
  supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).options(joinedload(models.Supplier.products)).first()

  if supplier is None:
    raise HTTPException(404)
  
  total_sells = func.sum(models.Order.amount).label('total_sells')
  
  most_selled_items = db.query(models.Supplier.id, models.Supplier.id, models.Product.name, models.Product.rating, models.Product.picture, models.Product.price, total_sells)\
    .join(models.Product, models.Product.supplier_id == models.Supplier.id).join(models.Order, models.Order.product_id == models.Product.id)\
    .group_by(models.Supplier.id, models.Product.name, models.Product.rating, models.Product.picture, models.Product.price).order_by(total_sells).limit(5).all()
  
  return {
    'supplier': supplier,
    'most_selled_items': most_selled_items
  }