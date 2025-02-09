"""
This module provides a PostgreSQL database connection using SQLAlchemy.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from logger import Logger

load_dotenv()


class PostgreSQL:
    def __init__(self):
        """
        Initialize database connection parameters and logger.
        """
        self.hostname = os.getenv("DB_HOSTNAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")
        self.connection_str = (
            f"postgresql+psycopg2://{self.user}:{self.password}@"
            f"{self.hostname}:5432/{self.database}"
        )

        self.logger_instance = Logger("database_logger", "database.log")
        self.logger = self.logger_instance.get_logger()
        self.engine = None

    def get_engine(self):
        """
        Creates and returns a SQLAlchemy engine for the PostgreSQL database.

        Returns:
        engine: The SQLAlchemy engine for the PostgreSQL database.

        Raises:
        SQLAlchemyError: If an error occurs while creating the engine.
        """

        if not self.engine:
            try:
                self.engine = create_engine(self.connection_str)
                self.logger.info("Connection successfully")
                return self.engine

            except SQLAlchemyError as e:
                self.logger.error(f"Database connection failed: {str(e)}")
                raise RuntimeError("Could not connect to the database")

        return self.engine
