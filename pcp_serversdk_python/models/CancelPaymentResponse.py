from typing import Optional
from dataclasses import dataclass
from .PaymentResponse import PaymentResponse

@dataclass(kw_only=True)
class CancelPaymentResponse:
    payment: Optional[PaymentResponse] = None
