from enum import Enum


class UnscheduledCardOnFileRequestor(Enum):
    MERCHANT_INITIATED = "merchantInitiated"
    CARDHOLDER_INITIATED = "cardholderInitiated"
