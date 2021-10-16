from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, Integer, String, func

from trading_db.rdb.base import Model


class Firm(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    trading_fee = Column(Float, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    __tablename__ = "firms"

    def soft_delete(self):
        self.deleted_at = datetime.now(tz=timezone.utc)
