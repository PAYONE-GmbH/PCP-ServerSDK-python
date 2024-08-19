from enum import Enum


class PaymentStatus(Enum):
    WAITING_FOR_PAYMENT = "WAITING_FOR_PAYMENT"
    PAYMENT_NOT_COMPLETED = "PAYMENT_NOT_COMPLETED"
    PAYMENT_COMPLETED = "PAYMENT_COMPLETED"
    NO_PAYMENT = "NO_PAYMENT"
