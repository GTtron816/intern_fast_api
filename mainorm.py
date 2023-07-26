from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import  models
import schema

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
    return characters
    
  

@app.get('/{id}')
def get_user(id:int,db: Session = Depends(get_db)):
    characters=db.query(models.Characater).filter(models.Characater.cid == id).first()
    return [characters]
 
        
@app.post('/')
def add_item(item:schema.Character,db: Session = Depends(get_db)):
    new_character=models.Characater(**item.dict())
    db.add(new_character)
    db.commit()

@app.put('/{id}')
def update_item(id:int,item:schema.Character,db: Session = Depends(get_db)):
    db.query(models.Characater).filter(models.Characater.cid == id).update({**item.dict()})
    db.commit()
     