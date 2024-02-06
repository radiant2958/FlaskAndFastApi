import databases
from sqlalchemy import create_engine, MetaData


DATABASE_URL = "sqlite:///my_data.db"

database = databases.Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)



