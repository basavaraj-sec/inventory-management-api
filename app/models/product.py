
from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    # The database creates this ID automatically for each product.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    # SKU should be different for every product.
    sku = Column(String(50), unique=True, nullable=False, index=True)