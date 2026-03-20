from fastapi import FastAPI
from dbcnctn import get_connection
from app.api.routes import router

app.include_router(router)   #real endpoints

app = FastAPI()

@app.get("/test-db")  #Debugging DB connection
def test_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        return {"status": "connected", "result": result[0]}
    except Exception as e:
        return {"error": str(e)}