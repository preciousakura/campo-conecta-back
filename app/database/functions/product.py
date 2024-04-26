from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.Product import BaseProduct
from app import models

def create(db: Session, product: BaseProduct):
  db_product = models.Product(**product.model_dump(), picture='https://images.unsplash.com/photo-1603186741833-4a7cf699a8eb?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product
