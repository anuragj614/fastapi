# from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     # return {'hello': 'world'}
#     return 'Hi there! This is a FastAPI application.'

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = "Hello"):
#     return {'item_id': item_id, 'q': q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item_name":item.name, "item_price": item.price, "item_offer": item.is_offer}

