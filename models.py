from sqlalchemy import Column, Integer, String,Float
from database import Base


class Items(Base):
    __tablename__ = "Items"

    itm_id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True,unique=True)
    quantity = Column(Integer)
    price = Column(Integer) # in paise

class Offer(Base):
    __tablename__ = "Offer"

    offer_id = Column(Integer, primary_key=True, index=True)
    offer_type = Column(String)
    offer_val = Column(Float)
    
