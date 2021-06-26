from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title='Shopping Basket',description='API to calculate total of order',version='0.0.1')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#------------------------------Items--------------------------------------------

@app.post("/items/",tags=["Items"])
def insert_items(items: schemas.ItemExecute, db: Session = Depends(get_db)):
    items = crud.insert_items(db=db, items=items)
    return items

@app.get("/items/{itm_id}",tags=["Items"])
def read_item(itm_id: int, db: Session = Depends(get_db)):
    item = crud.get_item_by_id(db, itm_id=itm_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item {itm_id} not yet registered")
    return item

@app.get("/items/",tags=["Items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_all_items(db, skip=skip, limit=limit)
    return items

#-----------------------------------------------------------------------------

@app.post("/calculate_total/",tags=["CalculateOrderTotal"])
def calc_total(calc_details: schemas.CalcBase, db: Session = Depends(get_db)):
    order_total = crud.calculate_total(db=db, calc_details=calc_details)
    return order_total

#---------------------------Offers------------------------------------------------

@app.post("/offer/",tags=["Offers"])
def insert_offer(offers: schemas.OfferExecute, db: Session = Depends(get_db)):
    offers = crud.insert_offer_details(db=db, offers=offers)
    return offers

@app.get("/offer/{offer_id}",tags=["Offers"])
def read_offer_by_ID(offer_id: int, db: Session = Depends(get_db)):
    offer = crud.get_offer_by_id(db, offer_id=offer_id)
    if offer is None:
        raise HTTPException(status_code=404, detail=f"Offer {offer_id} not yet registered")
    return offer

@app.get("/offers/",tags=["Offers"])
def read_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = crud.get_all_offers(db, skip=skip, limit=limit)
    return offers
