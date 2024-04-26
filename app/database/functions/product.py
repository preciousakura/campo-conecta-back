from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.schemas.Product import BaseProduct
from app.schemas.Utils import Order
from app import models
import math

def create(db: Session, product: BaseProduct):
  db_product = models.Product(**product.model_dump(), picture='https://images.unsplash.com/photo-1603186741833-4a7cf699a8eb?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product

def update(db: Session, product_id: int, product: BaseProduct):
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
  