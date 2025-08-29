from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

# Create a SQLite database (stored as a file)
DATABASE_URL = "sqlite:///buildsmart.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL statements in terminal

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance to interact with the database
session = Session()

# Create all tables in the database
def create_tables():
    Base.metadata.create_all(engine)
