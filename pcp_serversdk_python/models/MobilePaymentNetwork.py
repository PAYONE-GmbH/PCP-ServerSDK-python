from enum import Enum


class MobilePaymentNetwork(str, Enum):
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"
    AMEX = "AMEX"
    GIROCARD = "GIROCARD"
    DISCOVER = "DISCOVER"
    JCB = "JCB"
