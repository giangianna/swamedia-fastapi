from fastapi import FastAPI
from app.api.v1.endpoints import router as api_v1_router
from app.core.database import init_db

app = FastAPI(
    title="My REST API",
    description="Standar REST API dengan FastAPI dan versioning",
    version="1.0.0"
)

# Generate tabel otomatis saat server dijalankan
@app.on_event("startup")
def startup():
    init_db()

# Include API versioning
app.include_router(api_v1_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
