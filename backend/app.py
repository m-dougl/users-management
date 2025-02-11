"""
This module sets up the FastAPI application and configures the database connection.
"""

import uvicorn
import models
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from crud import create_user, get_user, get_users, update_user, delete_user
from schemas import User, UserCreate
from database import PostgreSQL
from typing import List

database_handler = PostgreSQL()
logger = database_handler.logger
engine = database_handler.get_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)


def get_db():
    """
    Provides a database session for dependency injection.

    Yields:
    db (Session): The SQLAlchemy session object for database operations.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db=db, user=user)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        )


@app.get("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def read_user_api(user_id: int, db: Session = Depends(get_db)):
    try:
        user = get_user(db=db, user_id=user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {user_id} not found",
            )
        return user
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        )


@app.get("/users", response_model=List[User], status_code=status.HTTP_200_OK)
async def read_users_api(
    db: Session = Depends(get_db), offset: int = 0, limit: int = 100
):
    try:
        return get_users(db=db, offset=offset, limit=limit)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        )


@app.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def update_user_api(user_id: int, user: User, db: Session = Depends(get_db)):
    try:
        return update_user(db=db, user_id=user_id, user=user)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        )


@app.delete("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    try:
        return delete_user(db=db, user_id=user_id)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
        )
    except Exception as e:
        logger.error(f"User not found: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found: {e}"
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
