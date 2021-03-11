from __future__ import annotations

import csv
import datetime
from dataclasses import dataclass
from typing import List

# https://www.investing.com/crypto/bitcoin/historical-data


def get_data_from_csv(filename: str) -> List[PriceData]:
    result = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(PriceData.of(row))
    return result


def insert_data_to_db():
    pass


def str_to_float(float_str: str):
    float_str = float_str.replace(",", "")
    if "K" in float_str:
        float_str = float_str.replace("K", "")
        return float(float_str) * 1000
    if "M" in float_str:
        float_str = float_str.replace("M", "")
        return float(float_str) * 1000000
    return float(float_str)


@dataclass
class PriceData:
    date: datetime.datetime
    price: float
    open: float
    high: float
    low: float
    volume: float
    change: float

    @classmethod
    def of(cls, data: List[str]):
        return cls(
            date=datetime.datetime.strptime(data[0], "%Y-%m-%d"),
            price=str_to_float(data[1]),
            open=str_to_float(data[2]),
            high=str_to_float(data[3]),
            low=str_to_float(data[4]),
            volume=str_to_float(data[5]),
            change=str_to_float(data[6]),
        )
