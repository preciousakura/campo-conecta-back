from sqlalchemy import Column, String, Integer
from app.database.connection import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  email = Column(String, unique=True, index=True, nullable=False)
  password = Column(String, nullable=False)
  name = Column(String, nullable=False)
  last_name = Column(String, nullable=False)
