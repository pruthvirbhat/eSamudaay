from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
import schemas
import pandas as pd
#--------------------Items-------------------------

def insert_items(db: Session, items: schemas.ItemExecute):
    _db = models.Items(
    name = items.name,
    quantity = items.quantity,
    price = items.price
    )
    db.add(_db)
    db.commit()
    db.refresh(_db)
    
    return items

def get_item_by_id(db: Session, itm_id: int):
    return db.query(models.Items).filter(models.Items.itm_id==itm_id).first()

def get_all_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Items).offset(skip).limit(limit).all()

#--------------------Offers-------------------------

def insert_offer_details(db: Session, offers: schemas.OfferExecute):
    _db_offer = models.Offer(
    offer_type = offers.offer_type,
    offer_val = offers.offer_val
    )
    db.add(_db_offer)
    db.commit()
    db.refresh(_db_offer)
    
    return offers

def get_offer_by_id(db: Session, offer_id: int):
    return db.query(models.Offer).filter(models.Offer.offer_id==offer_id).first()

def get_all_offers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Offer).offset(skip).limit(limit).all()


#----------------------------------------------------------------------
class DeliveryCostSlab:
    def __init__(self,distance) -> None:
        self.distance = distance

    def return_delivery_fee(self):
        if self.distance in range(0,10000):
            return 5000
        elif self.distance in range(10001,20000):
            return 10000
        elif self.distance in range(20001,50000):
            return 50000
        elif self.distance in range(50001,500000):
            return 100000


def calculate_total(db: Session, calc_details: schemas.CalcBase):
    items_list = calc_details.ordered_items
    delivery_distance = calc_details.distance
    offer_dict = calc_details.offer

    #Get the item total by adding cost for each item
    itm_total = 0
    for item in items_list:
        itm = get_item_by_id(db,item)
        if itm is None:
            raise HTTPException(status_code=404, detail=f"Item {item} not yet registered")
        itm_total = itm_total + (itm.quantity * itm.price)
    
    #Add the delivery cost
    dobj = DeliveryCostSlab(delivery_distance)
    delivery_cost = dobj.return_delivery_fee()

    total_cost = itm_total + delivery_cost

    # Discount if any offer exists
    discount_val = 0
    if offer_dict:
        if offer_dict["offer_type"] == 'FLAT':
            discount_val = offer_dict["offer_val"]
        elif offer_dict["offer_type"] == 'DELIVERY':
            discount_val = delivery_cost

    discount_val = min(discount_val,total_cost)
    total_cost = total_cost - discount_val
    return {"Order Total":total_cost}

