from typing import Optional
from dataclasses import dataclass
from .PaymentProduct840SpecificOutput import PaymentProduct840SpecificOutput


@dataclass(kw_only=True)
class RedirectPaymentMethodSpecificOutput:
    paymentProductId: Optional[int] = None
    paymentProduct840SpecificOutput: Optional[PaymentProduct840SpecificOutput] = None
    paymentProcessingToken: Optional[str] = None
    reportingToken: Optional[str] = None
