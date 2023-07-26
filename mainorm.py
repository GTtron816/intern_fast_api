from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import  models
import schema

from database import SessionLocal, engine,get_db


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
    
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



@app.get('/',response_model=List[schema.Response])
def get_user(db: Session = Depends(get_db)):
    characters=db.query(models.Characater).all()
    return characters
    
  

@app.get('/{id}',response_model=List[schema.Response])
def get_user(id:int,db: Session = Depends(get_db)):
    characters=db.query(models.Characater).filter(models.Characater.cid == id).first()
    return [characters]
 
        
@app.post('/',response_model=schema.PostResponse)
def add_item(item:schema.Character,db: Session = Depends(get_db)):
    new_character=models.Characater(**item.dict())
    db.add(new_character)
    db.commit()
    return new_character

@app.put('/{id}',response_model=schema.PostResponse)
def update_item(id:int,item:schema.Character,db: Session = Depends(get_db)):
    query=db.query(models.Characater).filter(models.Characater.cid == id)
    query.update({**item.dict()})
    db.commit()
    ret=query.first()
    return ret
     