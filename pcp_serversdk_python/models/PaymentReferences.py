from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class PaymentReferences:
    merchantReference: Optional[str] = None
    """Unique reference of payment transactions, also returned for reporting and
    reconciliation purposes. For capture requests, providing this value is
    recommended to support an end-to-end refund flow. If provided for captures or
    refunds, it must be unique per Checkout. Maximum length: 20 characters."""
