from dataclasses import dataclass
from typing import Optional

from .AmountOfMoney import AmountOfMoney


@dataclass(kw_only=True)
class PaymentLinkOrder:
    merchantReference: Optional[str] = None
    amount: Optional[AmountOfMoney] = None
