from typing import Dict, List, Optional
from pydantic import BaseModel
from datetime import datetime

#-----------------Items------------------------

class ItemBase(BaseModel):
    name: str
    quantity: int
    price: int
    
    class Config:
        schema_extra = {
            "example": {
                "name": "bread",
                "quantity": 2,
                "price": 2200
            }
        }
class ItemExecute(ItemBase):
    pass

class Items(ItemBase):
    itm_id: int   

    class Config:
        orm_mode = True


#-----------------Offers------------------------

class OfferBase(BaseModel):
    offer_type: str
    offer_val: float
    
    class Config:
        schema_extra = {
            "example": {
                "offer_type": "FLAT",
                "offer_val": 1000
            }
        }
class OfferExecute(OfferBase):
    pass

class Offers(OfferBase):
    offer_id: int   

    class Config:
        orm_mode = True


#-------------------------------------------------------------
class CalcBase(BaseModel):
    ordered_items: List
    distance: int
    offer: Optional[dict] = None
    class Config:
        schema_extra = {
            "example": {
                "ordered_items": [1,2],
                "distance": 1200,
                "offer": {
                    "offer_type": "FLAT",
                    "offer_val":1000
                }
            }
        }

