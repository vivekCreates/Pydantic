from pydantic import BaseModel,model_validator

class signup_data(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def check_password(self):
        if  self.password != self.confirm_password:
            raise ValueError("Password and confirm password should be same")
        return self
    
user = signup_data(password="1234",confirm_password="123")
print(user)