from dataclasses import dataclass
from typing import Optional

from .AmountOfMoney import AmountOfMoney
from .PaymentReferences import PaymentReferences


@dataclass(kw_only=True)
class PaymentIntentResponseData:
    amountOfMoney: Optional[AmountOfMoney] = None
    references: Optional[PaymentReferences] = None
    paymentIntentId: Optional[str] = None
    paymentId: Optional[str] = None
