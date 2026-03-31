from dataclasses import dataclass
from typing import Optional

from .PaymentReferences import PaymentReferences


@dataclass(kw_only=True)
class PaymentReferencesForRefund(PaymentReferences):
    """Object that holds all reference properties linked to this transaction."""

    captureReference: Optional[str] = None
    """Reference of the capture that should be used for the refund."""
