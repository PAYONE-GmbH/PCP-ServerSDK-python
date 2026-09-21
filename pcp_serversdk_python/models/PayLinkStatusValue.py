from enum import Enum


class PayLinkStatusValue(str, Enum):
    ACTIVE = "ACTIVE"
    PAID = "PAID"
    EXPIRED = "EXPIRED"
    REDIRECTED = "REDIRECTED"
