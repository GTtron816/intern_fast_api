from fastapi import FastAPI
import random
import psycopg2
import psycopg2.extras
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import  models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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


@app.get('/')
def get_user(db: Session = Depends(get_db)):
    characters=db.query(models.Characater).all()
    print(characters)
    return {"data":characters}
    
  

@app.get('/{id}')
def get_user(id:int):
    pass
 
        
@app.post('/')
def add_item(item:Character):
    pass

    


@app.put('/{id}')
def update_item(id:int,item:Character):
    pass
     
     