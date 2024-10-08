from enum import Enum


class StatusValue(str, Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    REJECTED_CAPTURE = "REJECTED_CAPTURE"
    REDIRECTED = "REDIRECTED"
    PENDING_PAYMENT = "PENDING_PAYMENT"
    PENDING_COMPLETION = "PENDING_COMPLETION"
    PENDING_CAPTURE = "PENDING_CAPTURE"
    AUTHORIZATION_REQUESTED = "AUTHORIZATION_REQUESTED"
    CAPTURE_REQUESTED = "CAPTURE_REQUESTED"
    CAPTURED = "CAPTURED"
    REVERSED = "REVERSED"
    REFUND_REQUESTED = "REFUND_REQUESTED"
    REFUNDED = "REFUNDED"
    REJECTED_REFUND = "REJECTED_REFUND"
    CANCELLATION_REQUESTED = "CANCELLATION_REQUESTED"
    PAUSED = "PAUSED"
    CHARGEBACKED = "CHARGEBACKED"
    CHARGEBACK_REVERSED = "CHARGEBACK_REVERSED"
    ACCOUNT_CREDITED = "ACCOUNT_CREDITED"
    ACCOUNT_DEBITED = "ACCOUNT_DEBITED"
    PAYOUT_REQUESTED = "PAYOUT_REQUESTED"
    REJECTED_CREDIT = "REJECTED_CREDIT"
