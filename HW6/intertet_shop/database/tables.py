from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import metadata


# Определение таблицы пользователей
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("surname", String, index=True),
    Column("email", String, unique=True, index=True),
  
)

# Определение таблицы товаров
items = Table(
    "items", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("description", String, index=True),
    Column("price", Float)
)

# Определение таблицы заказов
orders = Table(
    "orders", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("item_id", Integer, ForeignKey('items.id')),
    Column("order_date", String),
    Column("status", String)
)
