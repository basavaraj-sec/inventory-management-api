from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.product import Product


class ProductRepository:

    def create(self, db: Session, product: Product) -> Product:
        try:
            db.add(product)
            db.commit()
            db.refresh(product)

            return product

        except IntegrityError:
            # Undo the failed transaction before returning the error.
            db.rollback()
            raise ValueError("Product with this SKU already exists")

    def get_all(self, db: Session) -> list[Product]:
        return db.query(Product).all()

    def get_by_id(self, db: Session, product_id: int) -> Product | None:
        return db.query(Product).filter(Product.id == product_id).first()

    def update(
        self,
        db: Session,
        product: Product,
        product_data: dict
    ) -> Product:
        for field, value in product_data.items():
            setattr(product, field, value)

        db.commit()
        db.refresh(product)
        return product

    def delete(self, db: Session, product: Product) -> None:
        db.delete(product)
        db.commit()