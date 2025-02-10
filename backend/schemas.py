"""
This module defines Pydantic models (schemas) for the application.
"""

from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    """
    A base model for user data.

    Attributes:
    username (str): The username of the user.
    birth_date (datetime): The birth date of the user.
    email (EmailStr): The email address of the user.
    """

    username: str
    birth_date: date
    email: EmailStr


class UserCreate(UserBase):
    """
    A model for creating a new user, inheriting from UserBase.
    """

    pass


class User(UserBase):
    """
    A model representing a user with an additional ID attribute, inheriting from UserBase.

    Attributes:
    id (int): The unique identifier for the user.
    """

    id: int
