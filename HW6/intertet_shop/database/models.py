from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database.db import database
from datetime import datetime

class User(database):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Item(database):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)

class Order(database):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

    user = relationship("User")
    item = relationship("Item")
