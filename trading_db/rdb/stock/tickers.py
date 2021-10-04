import enum
from typing import TYPE_CHECKING

from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..base import Model

if TYPE_CHECKING:
    from ..stock_firm.firm import Firm


class StockType(enum.Enum):
    STOCK = "STOCK"
    ETF = "ETF"


class StockTicker(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_type = Column(
        Enum(StockType, native_enum=False, create_constraint=False),
        nullable=False,
    )
    ticker = Column(String(255), nullable=False)
    firm_id = Column(Integer, ForeignKey("firms.id"))
    fee = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)

    firm: Firm = relationship("Firm")

    __tablename__ = "tickers"
