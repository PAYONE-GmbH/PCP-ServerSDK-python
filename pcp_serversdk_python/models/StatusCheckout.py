from enum import Enum


class StatusCheckout(Enum):
    OPEN = "OPEN"
    PENDING_COMPLETION = "PENDING_COMPLETION"
    COMPLETED = "COMPLETED"
    BILLED = "BILLED"
    CHARGEBACKED = "CHARGEBACKED"
    DELETED = "DELETED"
