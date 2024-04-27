from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from app.dependencies import get_db, get_current_user
from app.schemas.order import OrderCreate, Order, OrderWithRelations
from app.schemas.utils import Pageable
from app.database.functions import order

router = APIRouter(
  prefix='/order',
  tags=['order']
)

@router.post('', status_code=201, response_model=Order)
def create_order(user_id: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)], order_info: OrderCreate):
  return order.create(db, user_id, order_info)

@router.get('', status_code=200, response_model=Pageable[OrderWithRelations])
def get_user_orders(
  user_id: Annotated[int, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)],
  page: Annotated[int, Query(ge=0)] = 0, size: Annotated[int, Query(gt=0)] = 10,
  last_months: Annotated[int | None, Query(ge=1, description='Filtrar pedidos criados nos ultimos X meses')] = None,
  search: str | None = None
):
  return order.get_user_orders(db, user_id, page, size, last_months, search)
