from pydantic import BaseModel,Field



class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Employee name",
        examples="Vivek kumar"
    )
    
    email : str = Field(
        ...,
        regex=r""
    )
    
    salary: int = Field(
        ...,
        ge=10000,
        description="Employee salary"
    )
    

