from sqlalchemy import BigInteger, Column, Date, Float
from sqlalchemy.sql import functions as sqlfuncs

from .base import Model


class Bitcoin(Model):
    id = Column(BigInteger, primary_key=True)
    price = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    change = Column(Float, nullable=False)
    date = Column(Date, nullable=False, default=sqlfuncs.now(), index=True)

    __tablename__ = "bitcoin"
