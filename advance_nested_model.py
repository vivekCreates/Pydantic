from pydantic import BaseModel
from typing import List,Optional,Union


class Address(BaseModel):
    city: str
    village: str
    pin_code:str
    
class Company(BaseModel):
    name: str
    Address: Optional[Address]
    
class Employee(BaseModel):
    name:str
    company:Optional[Company]
    
    
class TextContent(BaseModel):
    type:str = "text"
    content: str
    
class ImageContent(BaseModel):
    type:str = "image"
    url: str
    
class Article(BaseModel):
    name: str
    content:Optional[Union[TextContent,ImageContent]]