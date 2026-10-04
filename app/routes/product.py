from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductResult,
)
from app.services.product import ProductService
from app.repositories.product import ProductRepository


router = APIRouter()

# Keep service creation in one place so FastAPI can inject it into the routes.
def get_product_service() -> ProductService:
    return ProductService(ProductRepository())


@router.post(
    "/products",
    response_model=ProductResult,
    responses={
        409: {
            "description": "Product with this SKU already exists"
        }
    }
)
def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    product_service: ProductService = Depends(get_product_service)
):
    try:
        product = product_service.create_product(
            db,
            product_data
        )

    except ValueError as error:
        raise HTTPException(
            status_code=409,
            detail=str(error)
        )

     # Return a success message along with the newly created product.
    return {
        "message": "Product created successfully",
        "product": {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "sku": product.sku
        }
    }


@router.get(
    "/products",
    response_model=list[ProductResponse]
)
def get_products(
    db: Session = Depends(get_db),
    product_service: ProductService = Depends(get_product_service)
):
     # Ask the service for all products.
    products = product_service.get_all_products(db)

    return products


@router.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    product_service: ProductService = Depends(get_product_service)
):
    # Find the requested product through the service layer.
    product = product_service.get_product_by_id(
        db,
        product_id
    )

    if product is None:
        # Return 404 when the requested product does not exist.
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put(
    "/products/{product_id}",
    response_model=ProductResult
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
    product_service: ProductService = Depends(get_product_service)
):
    # Let the service handle the update operation.
    product = product_service.update_product(
        db,
        product_id,
        product_data
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    # Return the updated product along with a success message.
    return {
        "message": "Product updated successfully",
        "product": {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "sku": product.sku
        }
    }


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    product_service: ProductService = Depends(get_product_service)
):  
    # Ask the service to delete the requested product.
    deleted = product_service.delete_product(
        db,
        product_id
    )

    if not deleted:
        # Return 404 when there is no product with the given ID.
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }