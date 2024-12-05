import sqlalchemy as sa
import databases

db_url = ("sqlite:///./apibank.db")

database = databases.Database(db_url)
metadata = sa.MetaData()
engine = sa.create_engine(db_url, connect_args={"check_same_thread": False})
