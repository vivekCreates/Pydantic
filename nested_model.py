from pydantic import BaseModel


class Address(BaseModel):
    city: str
    village: str
    pin_code:str
    
class User(BaseModel):
    id: int
    name:str
    address:Address
    
    
address = Address(
    city="Bulandshahr",
    village="Imaliya",
    pin_code= "203001"
)

user = User(
    id=1,
    name="Rajat",
    address=address
)
    
print("user: ",user)