# coding: utf-8

from database import Base, engine
from sqlalchemy import (
    Boolean, Column, ForeignKey, Integer, String, text, Sequence
)
from sqlalchemy.orm import relationship


class ProductType(Base):
    __tablename__ = 'product_type'

    type_id_seq = Sequence('product_type_type_id_seq', metadata=Base.metadata)

    type_id = Column(
        Integer,
        type_id_seq,
        # server_default=type_id_seq.next_value(),
        primary_key=True
    )
    type_name = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(128))


class ProductClass(Base):
    __tablename__ = 'product_class'

    class_id_seq = Sequence('product_class_class_id_seq', metadata=Base.metadata)

    class_id = Column(
        Integer,
        class_id_seq,
        # server_default=class_id_seq.next_value(),
        primary_key=True
    )
    type_id = Column(ForeignKey('product_type.type_id'), nullable=False)
    class_name = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(128))
    is_system = Column(Boolean)

    type = relationship('ProductType')
