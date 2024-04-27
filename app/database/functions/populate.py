from sqlalchemy.orm import Session
from app import models
import json
import os

def populate_suppliers(db: Session):
  with open(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'suppliers.json'), 'r') as file:
    suppliers = json.load(file)
    for supplier in suppliers:
      new_supplier = models.Supplier(**supplier)
      db.add(new_supplier)
    db.commit()

  return 'populated'

def populate_products(db: Session):
  with open(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'products.json'), 'r') as file:
    products = json.load(file)
    for product in products:
      new_product = models.Product(**product)
      db.add(new_product)
    db.commit()

  return 'populated'

def populate_orders(db: Session, user_id: int):
  with open(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'orders.json'), 'r') as file:
    products = json.load(file)
    for product in products:
      new_product = models.Order(**product, user_id=user_id)
      db.add(new_product)
    db.commit()

  return 'populated'
