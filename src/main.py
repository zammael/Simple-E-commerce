from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    

class Item(BaseModel):
    name: str
    price: float
    

class Order(BaseModel):
    product: str
    user: str
    total: float


user_list = []
item_list = []
order_list = []


@app.get("/")
def root():
    response = {"message": "Hello World"}
    print(response["message"])
    return response


@app.post("/user")
def create_user(user: User):
    user_list.append(user)
    response = {
        "statusCode": 201,
        "data": user
        }
    return response


@app.get("/user")
def get_user():
    response = {
        "statusCode": 200,
        "data": user_list
    }
    return response


@app.post("/item")
def create_item(item: Item):
    item_list.append(item)
    response = {
        "statusCode": 201,
        "data": item
        }
    return response


@app.get("/item")
def get_item():
    response = {
        "statusCode": 200,
        "data": item_list
    }
    return response


@app.post("/order")
def create_order(order: Order):
    order_list.append(order)
    response = {
        "statusCode": 201,
        "data": order
        }
    return response


@app.get("/order")
def get_order():
    response = {
        "statusCode": 200,
        "data": order_list
    }
    return response
