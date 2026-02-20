from dataclasses import dataclass


@dataclass(kw_only=True)
class PausePaymentRequest:
    """Request to pause a payment for a specific payment method."""
