from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .model import Product

def get_product_by_barcode(db: Session, barcode: str):
    return db.query(Product).filter(Product.barcode == barcode).first()


def create_product(db: Session, product):
    existing_product = get_product_by_barcode(db, product.barcode)
    
    if existing_product:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product with this barcode already exists"
            )
        
    new_product = Product(
        name=product.name,
        barcode=product.barcode,
        category=product.category,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product




def delete_product(db: Session, barcode: str):
    product = get_product_by_barcode(db, barcode)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

