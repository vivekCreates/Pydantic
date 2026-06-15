from pydantic import BaseModel
from typing import Optional,List


class Comment(BaseModel):
    id:int
    content:str
    replies: Optional[List[Comment]] = []
    
    
comment = Comment(
    id=1,
    content="Hello everyone",
    replies=[
        Comment(id=2,content="Learn fast"),
        Comment(id=3,content="Learn Agentic AI",replies=[
            Comment(
                id=4,
                content="I am learing you learn first"
                
            )
        ])
    ]
)

print("comment: ",comment)