from typing import Optional
from dataclasses import dataclass, field
from .PaymentReferences import PaymentReferences
from .PositiveAmountOfMoney import PositiveAmountOfMoney
from .ReturnInformation import ReturnInformation

@dataclass(kw_only=True)
class RefundRequest:
    amountOfMoney: Optional[PositiveAmountOfMoney] = None
    references: Optional[PaymentReferences] = None
    # TODO: Check if this works for the reserved word
    return_: Optional[ReturnInformation] = field(default=None, metadata={'name': 'return'})
