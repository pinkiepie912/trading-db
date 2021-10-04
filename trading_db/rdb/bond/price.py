import enum

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    UniqueConstraint,
)

from trading_db.rdb.base import Model


class Currency(enum.Enum):
    USD = "USD"
    KRW = "KRW"


class StockType(enum.Enum):
    BOND = "BOND"
    ETF = "ETF"


class Bond(Model):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ticker_id = Column(Integer, ForeignKey("tickers.id"))
    stock_type = Column(String(255), nullable=False)
    adj_close = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    volume = Column(BigInteger, nullable=False)
    date_time = Column(DateTime(timezone=True), nullable=False)
    currency = Column(String(255), nullable=False)

    __tablename__ = "bonds"
    __table_args__ = (
        Index("ix_date_time_ticker_id", date_time.desc(), ticker_id),
        UniqueConstraint(
            "ticker_id", "date_time", name="uix_date_time_ticker_id"
        ),
    )
