from sqlalchemy import text
from app.db.database import engine

def test_connection():
    with engine.connect() as conn:
        return conn.execute(text("SELECT 1")).scalar()