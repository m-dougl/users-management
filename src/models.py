"""
This module defines the SQLAlchemy ORM models for the application.
"""

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Represents a user in the database.

    Attributes:
    __tablename__ (str): The name of the database table.
    id (Column): The unique identifier for the user.
    username (Column): The username of the user.
    birth_date (Column): The birth date of the user.
    email (Column): The email address of the user.
    """

    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String(50), nullable=False)
    birth_date = Column(Date)
    email = Column(String(50), nullable=False, unique=True)
