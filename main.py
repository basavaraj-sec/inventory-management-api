from fastapi import FastAPI

from app.database import Base, engine
from app.models.product import Product
from app.routes.product import router as product_router

# Make sure the required tables are available when the app starts.
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Connect the product routes to the main API.
app.include_router(product_router)


@app.get("/")
def home():
    return {
        "message": "Inventory Management API is running"
    }