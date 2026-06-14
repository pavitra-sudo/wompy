from sqlalchemy.orm import Session
from model import Product

def get_product_by_barcode(db: Session, barcode: str):
    return db.query(Product).filter(Product.barcode == barcode).first()


def create_product(db: Session, product_data):

    new_product = Product(
        name=product_data.name,
        barcode=product_data.barcode,
        category=product_data.category,
        description=product_data.description,
        price=product_data.price,
        quantity=product_data.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

