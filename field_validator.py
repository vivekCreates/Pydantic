from pydantic import BaseModel,field_validator


class User(BaseModel):
    username: str
    
    @field_validator("username")
    def check_username_length(cls,v):
        if  len(v) < 3:
            raise ValueError("Username must be of 3 characters")
        return v
    
user = User(username="abd")
print(user)