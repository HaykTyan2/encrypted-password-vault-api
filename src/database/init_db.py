from src.database.session import engine, Base
import src.database.models

def init_db():
    Base.metadata.create_all(bind=engine)
