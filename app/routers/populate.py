from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.dependencies import get_db
from app.database.functions import populate

router = APIRouter(
  prefix='/populate',
  tags=['populate']
)

@router.post('/suppliers', status_code=200)
def populate_suppliers(db: Annotated[Session, Depends(get_db)]):
  return populate.populate_suppliers(db)

@router.post('/products', status_code=200)
def populate_products(db: Annotated[Session, Depends(get_db)]):
  return populate.populate_products(db)

@router.post('/orders', status_code=200)
def populate_orders(db: Annotated[Session, Depends(get_db)], user_id: int):
  return populate.populate_orders(db, user_id)
