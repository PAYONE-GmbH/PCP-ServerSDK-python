from enum import Enum


class ExtendedCheckoutStatus(Enum):
    OPEN = "OPEN"
    DELETED = "DELETED"
    PENDING_COMPLETION = "PENDING_COMPLETION"
    COMPLETED = "COMPLETED"
    PARTIALLY_BILLED = "PARTIALLY_BILLED"
    BILLED = "BILLED"
    CHARGEBACKED = "CHARGEBACKED"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
    REFUNDED = "REFUNDED"
