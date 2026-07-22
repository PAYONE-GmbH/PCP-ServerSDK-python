from dataclasses import dataclass
from typing import Optional

from .AmountOfMoney import AmountOfMoney
from .PaymentReferences import PaymentReferences
from .ShoppingCartData import ShoppingCartData


@dataclass(kw_only=True)
class CreatePaymentIntent:
    amountOfMoney: Optional[AmountOfMoney] = None
    references: Optional[PaymentReferences] = None
    shoppingCart: Optional[ShoppingCartData] = None
