from sqlalchemy import Column, Integer, String

from database import Base
class Characater(Base):
    __tablename__ = "characters"
    cid=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    species=Column(String)
    year=Column(Integer)
    image=Column(String)