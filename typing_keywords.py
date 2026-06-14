from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id: int
    items:List[str]
    quantities:Dict[str,int]
     
     
class BlogPost(BaseModel):
    user_id: int
    title:str
    description: Optional[str] = None
    

cart_data = {
    "user_id":1,
    "items":["Keyboard","mouse","Laptop stand"],
    "quantities":{
        "keyboard":1,
        "mouse":1,
        "Laptop stand":2
    }
}

post_data = {
    "user_id":2,
    "title":"Agentic AI"
}
cart = Cart(**cart_data)
post = BlogPost(**post_data)

print("Cart: ",cart)
print("Post: ",post)