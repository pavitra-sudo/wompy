from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schema import GetProduct ,PostProductRequest
from . import service  # Import the service layer

router = APIRouter()

@router.post("/", response_model=PostProductRequest)
def create_product(product: PostProductRequest, db: Session = Depends(get_db)):
    # Here you would call a service function to handle the creation logic
    product = service.get_product_by_barcode(db, product.barcode)
    if product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this barcode already exists"
        )
    new_product = service.create_product(db, product)



@router.get("/{barcode}", response_model=GetProduct)
def get_product(barcode: str, db: Session = Depends(get_db)):
    
    product = service.get_product_by_barcode(db, barcode)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found"
        )
        
    return product


