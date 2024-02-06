from datetime import datetime
import random
from typing import List
from fastapi import FastAPI
import database as models
from database.db import engine, database,metadata
from database import tables
from schema import shemas
from fastapi import HTTPException

metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

###USERS
    
# @app.get("/fake_users/{count}")
# async def create_user(count: int):
#     for i in range(count):
#         query = tables.users.insert().values(name=f'user{i}', surname=f'user{i}{i}',email = f'mail{i}@mail.ru' )
#         await database.execute(query)

#     return {'message': f'{count} fake users'}
    
@app.get("/users/", response_model=List[shemas.UserIn])  
async def read_users():
    query = tables.users.select()  
    return await database.fetch_all(query)  



@app.post("/users/", response_model=shemas.UserCreate)
async def create_user(user: shemas.UserCreate):
    db_user = await database.fetch_one(tables.users.select().where(tables.users.c.email == user.email))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    query = tables.users.insert().values(name=user.name, surname=user.surname, email=user.email)
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}

@app.put("/users/{user_id}", response_model=shemas.UserCreate)
async def update_user(user_id: int, user: shemas.UserCreate):
    db_user = await database.fetch_one(tables.users.select().where(tables.users.c.id == user_id))
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    query = tables.users.update().where(tables.users.c.id == user_id).values(name=user.name, surname=user.surname, email=user.email)
    await database.execute(query)
    return {**user.dict(), "id": user_id}


@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    db_user = await database.fetch_one(tables.users.select().where(tables.users.c.id == user_id))
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    query = tables.users.delete().where(tables.users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted successfully"}

##Items

# @app.get("/fake_items/{count}")
# async def create_items(count: int):
#     for i in range(count):
#         query = tables.items.insert().values(name=f'item{i}', description=f'description{i}',price = f'{i+100}' )
#         await database.execute(query)

#     return {'message': f'{count} fake items'}

    
@app.get("/items/", response_model=List[shemas.ItemIn])  
async def read_items():
    query = tables.items.select()  
    return await database.fetch_all(query)  




@app.post("/items/", response_model=shemas.Item)
async def create_item(item: shemas.Item):
    query = tables.items.insert().values(name=item.name, description=item.description, price=item.price)
    item_id = await database.execute(query)
    return {**item.dict(), "id": item_id}

@app.put("/items/{item_id}", response_model=shemas.Item)
async def update_item(item_id: int, item: shemas.ItemIn):
    db_item = await database.fetch_one(tables.items.select().where(tables.items.c.id == item_id))
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    query = tables.items.update().where(tables.items.c.id == item_id).values(name=item.name, description=item.description, price=item.price)
    await database.execute(query)
    return {**item.dict(), "id": item_id}

@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    db_item = await database.fetch_one(tables.items.select().where(tables.items.c.id == item_id))
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    query = tables.items.delete().where(tables.items.c.id == item_id)
    await database.execute(query)
    return {"message": "Item deleted successfully"}


###Oders

# @app.get("/fake_oders/{count}")
# async def create_oders(count: int):
#     user_ids = [1, 2, 3, 4, 5, 6, 7]  
#     item_ids = [1, 2, 3, 4, 5, 6, 7]
#     for i in range(count):
#         user_id = random.choice(user_ids)
#         item_id = random.choice(item_ids)
#         status = "pending"
#         # Установка даты заказа на текущее время
#         order_date = datetime.now()

#         query = tables.orders.insert().values(
#             user_id=user_id,
#             item_id=item_id,
#             status=status,
#             order_date=order_date
#         )

#         await database.execute(query)

#     return {'message': f'{count} fake orders created'}


@app.get("/orders/", response_model=List[shemas.Order])
async def read_orders():
    query = tables.orders.select()
    return await database.fetch_all(query)
    

@app.post("/orders/", response_model=shemas.Order)
async def create_order(order: shemas.OrderCreate):
    query = tables.orders.insert().values(
        user_id=order.user_id,
        item_id=order.item_id,
        status=order.status,
        order_date=datetime.now())  
    order_id = await database.execute(query)
    return {**order.dict(), "id": order_id}


@app.put("/orders/{order_id}", response_model=shemas.Order)
async def update_order(order_id: int, order: shemas.OrderCreate):
    db_order = await database.fetch_one(tables.orders.select().where(tables.orders.c.id == order_id))
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    query = tables.orders.update().where(tables.orders.c.id == order_id).values(
        user_id=order.user_id,
        item_id=order.item_id,
        status=order.status
    )
    await database.execute(query)
    return {**order.dict(), "id": order_id}


@app.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    db_order = await database.fetch_one(tables.orders.select().where(tables.orders.c.id == order_id))
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    query = tables.orders.delete().where(tables.orders.c.id == order_id)
    await database.execute(query)
    return {"message": "Order deleted successfully"}
