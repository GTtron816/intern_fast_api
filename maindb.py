from fastapi import FastAPI,Body
import random
import psycopg2
import psycopg2.extras
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
conn=psycopg2.connect(database="gt",host="localhost",user="postgres",password="root",port="5432")
cursor=conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
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
    cursor.execute("select * from characters")
    characters=cursor.fetchall()
    return characters

@app.get('/{id}')
def get_user(id:int):
    cursor.execute("select * from characters where cid={}".format(id))
    characters=cursor.fetchall()
    return characters
        
@app.post('/')
def add_item(item:Character):
    post_item=item.dict()
    post_item["cid"]=random.randint(0,10000)
    cursor.execute("insert into characters values({},'{}','{}',{},'{}')".format(post_item["cid"],post_item["name"],post_item["species"],post_item["year"],post_item["image"]))
    conn.commit()
    


@app.put('/{id}')
def update_item(id:int,item:Character):
     put_item=item.dict()
     cursor.execute("update characters  set name='{}',species='{}',year={},image='{}' where cid={}".format(put_item["name"],put_item["species"],put_item["year"],put_item["image"],id))
     conn.commit()
     

  