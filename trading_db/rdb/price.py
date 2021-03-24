import enum

from sqlalchemy import BigInteger, Column, Date, Float, Index, String

from .base import Model


class Currency(enum.Enum):
    USD = "USD"
    KRW = "KRW"


class Price(Model):
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    ticker = Column(String(255), nullable=False)
    adjclose = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    volume = Column(BigInteger, nullable=False)
    date = Column(Date, nullable=False)
    currency = Column(String(255), nullable=False)

    __tablename__ = "prices"
    __table_args__ = (
        Index("ix_date_name", date.desc(), name),
        Index("ix_date_ticker", date.desc(), name),
    )
