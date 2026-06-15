from pydantic import BaseModel,field_validator,model_validator


class Person(BaseModel):
    first_name:str
    last_name: str
    
    @field_validator("first_name","last_name")
    def check_len(cls,v):
        if len(v) < 3:
            raise ValueError("first_name and last_name must be atleast of 3 characters.")
        return v
    
    
class User(BaseModel):
    email:str
    
    @field_validator("email")
    def normalize_email(cls,v):
        return v.lower().strip()
    
    

class Product(BaseModel):
    name:str
    price:int
    quantity:int
    
    @model_validator(mode="after")
    def total_amount(self):
        return self.price * self.quantity
    