from fastapi import FastAPI
from app.api.routes import router
from app.dbcnctn import test_connection

app = FastAPI()
app.include_router(router)

@app.get("/test-db")
def test_db():
    try:
        result = test_connection()
        return {"status": "connected", "result": result}
    except Exception as e:
        return {"error": str(e)}