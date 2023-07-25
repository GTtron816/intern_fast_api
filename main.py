from fastapi import FastAPI,Body
import random
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
class Character(BaseModel):
    name:str
    species:str
    year:int
    image:str
    # def __getitem__(self,item):
    #     return getattr(self,item)
    
app=FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

characters=[]
def create_char():
  item1 =	{
  "cid":100,
  "name": "Harry Potter",
  "species": "Human",
  "year": 1964,
  "image":"https://ik.imagekit.io/hpapi/harry.jpg"}
  item2 =	{
  "cid":200,
  "name": "Hermione Granger",
  "species": "Human",
  "year": 1954,
  "image":"https://ik.imagekit.io/hpapi/hermione.jpeg"}
  characters.append(item1)
  characters.append(item2)
create_char()

@app.get('/')
def get_user():
    return characters

@app.get('/{id}')
def get_user(id:int):
    for i in characters:
        if i["cid"] == id:
            return [i]
        
@app.post('/')
def add_item(item:Character):
    post_item=item.dict()
    post_item["cid"]=random.randint(0,10000)
    characters.append(post_item)


@app.put('/{id}')
def update_item(id:int,item:Character):
     index=int(getIndex(id))
     put_item=item.dict()
     put_item["cid"]=id
     characters[index]=put_item
     
def getIndex(id):
    for i,x in enumerate(characters):
        if x["cid"] == id:
            return i
    
          
                
            
            