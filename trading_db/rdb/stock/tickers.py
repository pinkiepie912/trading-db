from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.hybrid import hybrid_property
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
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    firm: Firm = relationship("Firm")

    __tablename__ = "tickers"

    def soft_delete(self):
        self.deleted_at = datetime.now(tz=timezone.utc)

    @hybrid_property
    def is_active(self) -> bool:
        return self.deleted_at is None

    @is_active.expression  # type: ignore
    def is_active(cls) -> bool:
        return cls.deleted_at.is_(None)
