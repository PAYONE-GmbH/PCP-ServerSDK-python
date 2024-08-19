from typing import Optional
from dataclasses import dataclass
from .PaymentProduct3392SpecificInput import PaymentProduct3392SpecificInput

@dataclass(kw_only=True)
class FinancingPaymentMethodSpecificInput:
    paymentProductId: Optional[int] = None
    requiresApproval: Optional[bool] = True
    paymentProduct3392SpecificInput: Optional[PaymentProduct3392SpecificInput] = None
