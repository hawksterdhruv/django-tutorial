# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    url = Column(String(200))
    data = Column(String(4000))
    created_date = Column(DateTime)
