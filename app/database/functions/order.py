from fastapi import HTTPException
from datetime import datetime, timedelta
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from app.schemas.order import OrderCreate
from app import models
import math

def calculate_discount(amount: int):
  if amount >= 2000:
    return 0.85
  elif amount >= 1000:
    return 0.90
  elif amount >= 500:
    return 0.95
  else:
    return 1

def create(db: Session, user_id: int, order_info: OrderCreate):
  order_product = db.query(models.Product).filter(models.Product.id == order_info.product_id).first()

  if order_product is None:
    raise HTTPException(404)

  order_product.total_selled += order_info.amount
  order_product.total_orders += 1
  order_product.delivery_price = 25 + (1 / (order_product.total_orders + 1)) * 25

  new_order = models.Order(
    amount=order_info.amount,
    product_id=order_info.product_id,
    user_id=user_id
  )
  db.add(new_order)
  db.commit()
  db.refresh(new_order)

  return new_order

def get_user_orders(db: Session, user_id: int, page: int, size: int, last_months: int | None, search: str | None = None):
  items_query = db.query(models.Order).filter(models.Order.user_id == user_id)

  if last_months is not None:
    month_limit = datetime.today() - timedelta(days=(last_months * 30))
    items_query = items_query.filter(models.Order.created_at > month_limit)

  if search is not None:
    items_query = items_query.join(models.Product, models.Product.id == models.Order.product_id).filter(models.Product.name.ilike(f'%{search}%'))

  total = items_query.with_entities(func.count(models.Order.id)).scalar()
  pages = math.ceil(total / size)

  items = items_query.offset(page * size).limit(size).options(joinedload(models.Order.product)).all()

  return {
    'items': items,
    'total': total,
    'pages': pages,
    'size': size,
    'page': page
  }