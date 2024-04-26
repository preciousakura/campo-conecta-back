from pydantic import BaseModel
from typing import Generic, TypeVar
from enum import Enum

T = TypeVar('T')

class Pageable(BaseModel, Generic[T]):
  items: list[T]
  total: int
  pages: int
  page: int
  size: int

class Order(Enum):
  ASC = 'ASC'
  DESC = 'DESC'