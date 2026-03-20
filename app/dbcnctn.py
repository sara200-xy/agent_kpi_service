import os
import pyodbc

def get_connection():
    conn_str = os.getenv("DB_CONNECTION")
    conn = pyodbc.connect(conn_str)
    return conn