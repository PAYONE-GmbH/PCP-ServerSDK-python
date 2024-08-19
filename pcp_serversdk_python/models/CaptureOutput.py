from typing import Optional
from dataclasses import dataclass
from .AmountOfMoney import AmountOfMoney
from .PaymentReferences import PaymentReferences

@dataclass(kw_only=True)
class CaptureOutput:
    amountOfMoney: Optional[AmountOfMoney] = None
    merchantParameters: Optional[str] = None
    references: Optional[PaymentReferences] = None
    paymentMethod: Optional[str] = None
