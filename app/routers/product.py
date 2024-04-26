from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user
from app.schemas.Product import Product, BaseProduct
from app.database.functions import product

router = APIRouter(
  prefix='/product',
  tags=['product']
)

@router.post('', status_code=201, response_model=Product)
def create_product(_: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)], new_product: BaseProduct):
  return product.create(db, new_product)