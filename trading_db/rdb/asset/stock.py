from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

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
from ..constants import Currency

if TYPE_CHECKING:
    from ..stock.tickers import StockTicker


class StockAsset(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker_id = Column(Integer, ForeignKey("tickers.id"))
    description = Column(String(255), default="")
    purchase_price = Column(Float, nullable=False)
    sell_price = Column(Float, default=0.0)
    amount = Column(Integer, nullable=False)
    currency = Column(
        Enum(Currency, native_enum=False, create_constraint=False),
        nullable=False,
    )
    purchased_at = Column(DateTime(timezone=True), nullable=False)
    sold_at = Column(DateTime(timezone=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    ticker: StockTicker = relationship("StockTicker")

    __tablename__ = "stock_assets"

    def sotf_delete(self):
        self.deleted_at = datetime.now(tz=timezone.utc)

    @hybrid_property
    def is_active(self) -> bool:
        return self.deleted_at is None

    @is_active.expression  # type: ignore
    def is_active(cls) -> bool:
        return cls.deleted_at.is_(None)

    @hybrid_property
    def has_not_yet_sold(self) -> bool:
        return self.sold_at is None

    @has_not_yet_sold.expression  # type: ignore
    def has_not_yet_sold(cls) -> bool:
        return cls.sold_at.is_(None)
