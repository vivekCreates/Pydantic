from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    quantity:int
    in_stock: bool = True
    
    
product = Product(
    id=2,
    name="Keyboard",
    quantity=2
)

print("product: ",product)