from typing import Optional
from dataclasses import dataclass
from .PaymentProduct771SpecificOutput import PaymentProduct771SpecificOutput

@dataclass(kw_only=True)
class SepaDirectDebitPaymentMethodSpecificOutput:
    paymentProductId: Optional[int] = None
    paymentProduct771SpecificOutput: Optional[PaymentProduct771SpecificOutput] = None
