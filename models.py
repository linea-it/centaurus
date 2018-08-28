from sqlalchemy import Column, String, Integer
from database import Base


class Test(Base):
    __tablename__ = 'testing'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
