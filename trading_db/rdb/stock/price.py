from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Index,
    Integer,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from ..base import Model
from ..constants import Currency
from ..stock.tickers import StockTicker


class Price(Model):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ticker_id = Column(Integer, ForeignKey("tickers.id"))
    adj_close = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    volume = Column(BigInteger, nullable=False)
    date_time = Column(DateTime(timezone=True), nullable=False)
    currency = Column(
        Enum(Currency, native_enum=False, create_constraint=False),
        nullable=False,
    )

    ticker: StockTicker = relationship("StockTicker")

    __tablename__ = "prices"
    __table_args__ = (
        Index("ix_date_time_ticker_id", ticker_id, date_time.desc()),
        UniqueConstraint(
            "ticker_id", "date_time", name="uix_date_time_ticker_id"
        ),
    )
