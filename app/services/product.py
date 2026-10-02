from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(
        self,
        db: Session,
        product_data: ProductCreate
    ) -> Product:

        product = Product(
            name=product_data.name,
            price=product_data.price,
            quantity=product_data.quantity,
            sku=product_data.sku
        )

        return self.repository.create(db, product)

    def get_all_products(
        self,
        db: Session
    ) -> list[Product]:

        return self.repository.get_all(db)

    def get_product_by_id(
        self,
        db: Session,
        product_id: int
    ) -> Product | None:

        return self.repository.get_by_id(db, product_id)

    def update_product(
        self,
        db: Session,
        product_id: int,
        product_data: ProductUpdate
    ) -> Product | None:

        product = self.repository.get_by_id(db, product_id)

        if product is None:
            return None

        updated_product = self.repository.update(
            db,
            product,
            product_data.model_dump()
        )

        return updated_product

    def delete_product(
        self,
        db: Session,
        product_id: int
    ) -> bool:

        product = self.repository.get_by_id(db, product_id)

        if product is None:
            return False

        self.repository.delete(db, product)

        return True