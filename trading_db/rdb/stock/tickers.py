from sqlalchemy import Column, Float, ForeignKey, Integer, String

from trading_db.rdb.base import Model


class StockTicker(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(255), nullable=False)
    firm_id = Column(Integer, ForeignKey("firms.id"))
    fee = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)

    __tablename__ = "tickers"
