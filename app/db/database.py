from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

DB_CONNECTION = os.getenv("DB_CONNECTION")

if not DB_CONNECTION:
    # fallback (local dev) if you want to assemble it from parts
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")

    DB_CONNECTION = (
        "Driver={ODBC Driver 18 for SQL Server};"
        f"Server={DB_SERVER};"
        f"Database={DB_NAME};"
        f"Uid={DB_USERNAME};"
        f"Pwd={DB_PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
    )

params = urllib.parse.quote_plus(DB_CONNECTION)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")