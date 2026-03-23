from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api.routes import router
from app.dbcnctn import test_connection

APP_BASE_URL = "https://kpi-agent-service-sara-dehrgbfxcrbmcgck.eastus-01.azurewebsites.net.azurewebsites.net" 

app = FastAPI(
    title="Pipeline KPI API",
    version="1.0.0",
    openapi_version="3.0.3", 
)

app.include_router(router)

@app.get("/test-db")
def test_db():
    try:
        result = test_connection()
        return {"status": "connected", "result": result}
    except Exception as e:
        return {"error": str(e)}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )

    # Hard set OpenAPI version (some generators override this)
    schema["openapi"] = "3.0.3"

    #Critical for Foundry: tell it where the API lives
    schema["servers"] = [{"url": APP_BASE_URL}]

    app.openapi_schema = schema
    return app.openapi_schema

app.openapi = custom_openapi