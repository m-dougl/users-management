"""
This module provides CRUD (Create, Read, Update, Delete) operations for the User model.
"""

from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models import User


def create_user(db: Session, user: UserCreate) -> User:
    """
    Creates a new user in the database using the provided user data.

    Parameters:
    db (Session): The SQLAlchemy session object for database operations.
    user (UserCreate): The data for the new user.

    Returns:
    User: The newly created user object.
    """

    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> User:
    """
    Retrieves a user from the database based on the provided user ID.

    Parameters:
    db (Session): The SQLAlchemy session object for database operations.
    user_id (int): The unique identifier of the user to be retrieved.

    Returns:
    User: The user object with the specified ID, or None if no user is found.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, offset: int = 0, limit: int = 100):
    """
    Retrieves a list of users from the database with pagination support.

    Parameters:
    db (Session): The SQLAlchemy session object for database operations.
    offset (int): The number of records to skip before starting to return records. Default is 0.
    limit (int): The maximum number of records to return. Default is 100.

    Returns:
    List[User]: A list of user objects.
    """

    return db.query(User).offset(offset).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserCreate):
    """
    Updates an existing user in the database with the provided user data.

    Parameters:
    db (Session): The SQLAlchemy session object for database operations.
    user_id (int): The unique identifier of the user to be updated.
    user (UserCreate): The new data for the user.

    Returns:
    User: The updated user object, or None if no user is found.
    """

    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        try:
            for key, value in user.model_dump().items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    return None


def delete_user(db: Session, user_id: int):
    """
    Deletes a user from the database based on the provided user ID.

    Parameters:
    db (Session): The SQLAlchemy session object for database operations.
    user_id (int): The unique identifier of the user to be deleted.

    Returns:
    bool: True if the user was successfully deleted, False if no user was found with the specified ID.

    Raises:
    SQLAlchemyError: If an error occurs during the database operation.
    """

    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        try:
            db.delete(db_user)
            db.commit()
            return True
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    return False
