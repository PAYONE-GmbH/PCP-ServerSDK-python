from enum import Enum


class AllowedPaymentActions(str, Enum):
    ORDER_MANAGEMENT = "ORDER_MANAGEMENT"
    PAYMENT_EXECUTION = "PAYMENT_EXECUTION"
