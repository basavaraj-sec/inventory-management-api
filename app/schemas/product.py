from pydantic import BaseModel

# Used when a new product is sent to the API.
class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    sku: str

# Used when an existing product is updated.
class ProductUpdate(BaseModel):
    name: str
    price: float
    quantity: int
    sku: str

# Defines the product data returned by the API.
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    sku: str

    # Allows Pydantic to read data directly from SQLAlchemy objects.
    model_config = {
        "from_attributes": True
    }

# Used for responses that contain a message along with the product.
class ProductResult(BaseModel):
    message: str
    product: ProductResponse