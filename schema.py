from pydantic import BaseModel
class Character(BaseModel):
    name:str
    species:str
    year:int
    image:str
class Response(BaseModel):
    cid:int
    name:str
    species:str
    year:int
    image:str
    class Config:
        orm_mode=True
class PostResponse(BaseModel):
    cid:int
    name:str
    class Config:
        orm_mode=True
   
    
    