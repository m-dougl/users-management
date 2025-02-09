from database import PostgreSQL
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String(50), nullable=False)
    birth_date = Column(DateTime)
    email = Column(String(50), nullable=False, unique=True)