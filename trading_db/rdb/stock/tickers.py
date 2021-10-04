from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..base import Model
from ..constants import Currency, StockType
from ..stock_firm.firm import Firm


class StockTicker(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_type = Column(
        Enum(StockType, native_enum=False, create_constraint=False),
        nullable=False,
    )
    name = Column(String(255), nullable=False)
    ticker = Column(String(255), nullable=False)
    currency = Column(
        Enum(Currency, native_enum=False, create_constraint=False),
        nullable=False,
    )
    firm_id = Column(Integer, ForeignKey("firms.id"))
    fee = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)

    firm: Firm = relationship("Firm")

    __tablename__ = "tickers"
