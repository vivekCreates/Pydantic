from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
    
user = User(
    id=1,
    name="vivek",
    is_active=True
)

print(user)