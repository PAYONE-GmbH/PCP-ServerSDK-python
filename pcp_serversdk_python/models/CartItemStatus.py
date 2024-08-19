from enum import Enum


class CartItemStatus(Enum):
    ORDERED = "ORDERED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    RETURNED = "RETURNED"
    WAITING_FOR_PAYMENT = "WAITING_FOR_PAYMENT"
