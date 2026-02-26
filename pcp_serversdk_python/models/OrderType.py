from enum import Enum


class OrderType(str, Enum):
    FULL = "FULL"
    PARTIAL = "PARTIAL"
