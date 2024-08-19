from enum import Enum


class ApplePayPaymentMethodType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"
    PREPAID = "prepaid"
    STORE = "store"
