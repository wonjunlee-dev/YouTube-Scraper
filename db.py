from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("PG_CONNECTION_STRING")

engine = create_engine(DB_URL)
Session = sessionmaker(bind = engine)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    return Session()
