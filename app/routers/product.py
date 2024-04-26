from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from app.dependencies import get_db, get_current_user
from app.schemas.Product import Product, BaseProduct, ProductUpdate
from app.schemas.Utils import Pageable, Order
from app.database.functions import product
from app.models import ProductType

router = APIRouter(
  prefix='/product',
  tags=['product']
)

@router.post('', status_code=201, response_model=Product)
def create_product(_: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)], new_product: BaseProduct):
  return product.create(db, new_product)

@router.put('/{product_id}', status_code=200, response_model=Product)
def update_product(_: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)], product_id: int, product_attrs: ProductUpdate):
  return product.update(db, product_id, product_attrs)

@router.get('', status_code=200, response_model=Pageable[Product])
def index_products(
  _: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)],
  page: Annotated[int, Query(ge=0)] = 0, size: Annotated[int, Query(gt=0)] = 10,
  min_price: Annotated[int | None, Query(ge=0)] = None, max_price: Annotated[int | None, Query(ge=0)] = None,
  price_order: Order | None = None, search: str | None = None, available: bool | None = None, product_type: ProductType | None = None
):
  return product.index(db, page, size, min_price, max_price, price_order, search, available)

@router.delete('/{product_id}', status_code=200, response_model=dict[str, bool])
def delete_product(_: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)], product_id: int):
  return product.delete(db, product_id)