from sqlalchemy import Column, ForeignKey, Integer, String

from trading_db.rdb.base import Model


class StockTicker(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(255), nullable=False)
    firm_id = Column(Integer, ForeignKey("firms.id"))

    __tablename__ = "tickers"
