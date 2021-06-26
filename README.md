# Application Server with FastAPI

## Run the application
python -m uvicorn main:app --reload

## View Result in Swagger GUI
port - http://127.0.0.1:8000/docs#/

## 1 Items

In Items we have a model which have basic data about the items. you get accessible via a rest API (CRUD) oprations. fields that are included in the model are -

* Name of the item
* Quantity of the item
* Prize

## API Overview
![Image of API Overview](https://github.com/pruthvirbhat/eSamudaay/blob/main/Images/API_main_file.png)

## Items List
![Image of Items List](https://github.com/pruthvirbhat/eSamudaay/blob/main/Images/Items_List.png)

## Calculates Total Order value
![Image of Total Order Value](https://github.com/pruthvirbhat/eSamudaay/blob/main/Images/Calculate_total.png)

# Technology stack
* FastAPI
* Python
