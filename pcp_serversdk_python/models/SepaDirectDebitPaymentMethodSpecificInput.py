from typing import Optional
from dataclasses import dataclass
from .SepaDirectDebitPaymentProduct771SpecificInput import SepaDirectDebitPaymentProduct771SpecificInput

@dataclass(kw_only=True)
class SepaDirectDebitPaymentMethodSpecificInput:
    paymentProduct771SpecificInput: Optional[SepaDirectDebitPaymentProduct771SpecificInput] = None
    paymentProductId: Optional[int] = None
