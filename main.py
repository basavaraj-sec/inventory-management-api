from fastapi import FastAPI

from app.database import Base, engine
from app.models.product import Product
from app.routes.product import router as product_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router)


@app.get("/")
def home():
    return {
        "message": "Inventory Management API is running"
    }