from dataclasses import dataclass
from typing import Optional

from .AmountOfMoney import AmountOfMoney
from .PaymentReferencesForPaymentIntent import PaymentReferencesForPaymentIntent
from .ShoppingCartData import ShoppingCartData


@dataclass(kw_only=True)
class CreatePaymentIntent:
    amountOfMoney: Optional[AmountOfMoney] = None
    references: PaymentReferencesForPaymentIntent
    shoppingCart: Optional[ShoppingCartData] = None
