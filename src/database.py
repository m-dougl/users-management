from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 
load_dotenv()

class PostgreSQL:
    def __init__(self):
        self.hostname = os.getenv('DB_HOSTNAME')
        self.user     = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_DATABASE')
        self.connection_str = f'postgresql+psycopg2://{self.user}:{self.password}@{self.hostname}/{self.database}'
        
    def get_engine(self):
        try:
            self.engine = create_engine(self.connection_str)
            return self.engine
        except Exception as e:
            return e

