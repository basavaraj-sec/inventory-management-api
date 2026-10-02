from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    sku: str

class ProductUpdate(BaseModel):
    name: str
    price: float
    quantity: int
    sku: str

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    sku: str

    model_config = {
        "from_attributes": True
    }

class ProductResult(BaseModel):
    message: str
    product: ProductResponse