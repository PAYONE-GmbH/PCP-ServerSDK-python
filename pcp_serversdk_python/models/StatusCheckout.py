from enum import Enum
from dataclasses import dataclass


class StatusCheckout(str, Enum):
    OPEN = "OPEN"
    PENDING_COMPLETION = "PENDING_COMPLETION"
    COMPLETED = "COMPLETED"
    BILLED = "BILLED"
    CHARGEBACKED = "CHARGEBACKED"
    DELETED = "DELETED"
