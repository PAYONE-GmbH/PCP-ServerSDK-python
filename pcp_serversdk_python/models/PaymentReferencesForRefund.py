from dataclasses import dataclass
from typing import Optional

from .PaymentReferences import PaymentReferences


@dataclass(kw_only=True)
class PaymentReferencesForRefund(PaymentReferences):
    """Object that holds all reference properties that are linked to this refund
    transaction. Extends the standard PaymentReferences with an additional
    captureReference field to support scenarios where a Checkout may contain multiple
    partial captures from different sellers."""

    captureReference: Optional[str] = None
    """Merchant-provided reference of the capture that this refund should be applied to.
        A single Checkout can contain multiple partial captures.
        By supplying the captureReference the merchant ensures the refund is allocated 
        to the correct capture.

        This value must match the merchantReference that was provided in the 
        PaymentReferences of the original capture request."""
