from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    barcode: str
    category: str | None = None
    description: str | None = None
    price: int 
    quantity: int
    
    
class GetProduct(ProductBase):
    id: int
    
    class Config:
        from_attributes = True
        
class PostProductRequest(ProductBase):
    pass

class PostProductResponse(BaseModel):
    id: int
    from_attributes = True
    
    