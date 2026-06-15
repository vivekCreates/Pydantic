from pydantic import BaseModel,ConfigDict
from typing import List 
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    pincode:str
    


class User(BaseModel):
    id:int
    name:str
    email:str
    password:str
    address:Address
    createdAt:datetime
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )
    
    
user = User(
    id=2,
    name="Vivek",
    email="vivek@gmail.com",
    password="123",
    createdAt=datetime.now(),
    address=Address(
        street="Imaliya",
        city="Bulandshahr",
        pincode="2030001"
    ),
    tags = ["premium","admin"] 
)

user_dict = user.model_dump()
user_json = user.model_dump_json()

print("user_dict: ",user_dict)
print("user_json: ",user_json)