from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from .schema import ( 
    GetProduct ,PostProductRequest, PostProductResponse
    )
from . import service  

router = APIRouter(prefix="/api/v1/product", tags=["products"])



@router.post("/", response_model=PostProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: PostProductRequest, db: Session = Depends(get_db)):
    
    new_product = service.create_product(db, product)
    return {
        "id": new_product.id,
        "msg": "Product created successfully"
    }
    
    
    
    
@router.delete("/{barcode}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(barcode: str, db: Session = Depends(get_db)):
    service.delete_product(db, barcode)
    




@router.get("/{barcode}", response_model=GetProduct, status_code=status.HTTP_200_OK)
def get_product(barcode: str, db: Session = Depends(get_db)):
    
    product = service.get_product_by_barcode(db, barcode)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found"
        )
    print(product)
    return product


