from dataclasses import dataclass
from typing import Optional

from .AmountOfMoney import AmountOfMoney
from .ShoppingCartData import ShoppingCartData


@dataclass(kw_only=True)
class PatchPaymentIntentRequest:
    amountOfMoney: Optional[AmountOfMoney] = None
    shoppingCart: Optional[ShoppingCartData] = None
