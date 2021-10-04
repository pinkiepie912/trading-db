import enum


class Currency(enum.Enum):
    USD = "USD"
    KRW = "KRW"


class StockType(enum.Enum):
    STOCK = "STOCK"
    ETF = "ETF"
