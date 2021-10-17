from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING, List

from sqlalchemy import Column, DateTime, Float, Integer, String, func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from trading_db.rdb.base import Model

if TYPE_CHECKING:
    from ..stock.tickers import StockTicker


class Firm(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    trading_fee = Column(Float, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    tickers: List[StockTicker] = relationship(
        "StockTicker",
        back_populates="firm",
        uselist=True,
        cascade="all, delete",
    )

    __tablename__ = "firms"

    def soft_delete(self):
        self.deleted_at = datetime.now(tz=timezone.utc)
        for ticker in self.tickers:
            if not ticker.is_active:
                continue
            ticker.soft_delete()

    @hybrid_property
    def is_active(self) -> bool:
        return self.deleted_at is None

    @is_active.expression  # type: ignore
    def is_active(cls) -> bool:
        return cls.deleted_at.is_(None)
