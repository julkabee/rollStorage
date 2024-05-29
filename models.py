from sqlalchemy import Integer, Date, Column
from sqlalchemy.orm import DeclarativeBase

from connect import engine


class Base(DeclarativeBase):
    pass


class Rolls(Base):
    __tablename__ = "rolls"
    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    weight = Column(Integer)
    add_dt = Column(Date)
    del_dt = Column(Date)


Base.metadata.create_all(bind=engine)
