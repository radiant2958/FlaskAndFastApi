from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)


class UserCreate(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    surname: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)




class ItemIn(BaseModel):
    name: str = Field( max_length=32)
    description: str = Field(max_length=128)
    price: float 


class Item(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    description: str = Field(..., max_length=128)
    price: float = Field(..., le=1000000)


class Order(BaseModel):
    user_id: int 
    item_id: int 
    order_date: str
    status: str = Field(max_length=32)


class OrderCreate(BaseModel):
    id: int
    user_id: int = Field(...)
    item_id: int = Field(...)
    order_date: Optional[str] = None
    status: str = Field(max_length=32)
    

    @validator('order_date', pre=True, allow_reuse=True)
    def datetime_to_string(cls, value):
        if value is None:
            return None
        elif isinstance(value, datetime):
            return value.isoformat()
        return value

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True  
  