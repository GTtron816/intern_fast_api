from pydantic import BaseModel
class Character(BaseModel):
    name:str
    species:str
    year:int
    image:str