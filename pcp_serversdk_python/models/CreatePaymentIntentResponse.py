from dataclasses import dataclass
from typing import Optional

from .PaymentIntentOutput import PaymentIntentOutput
from .ShoppingCartData import ShoppingCartData


@dataclass(kw_only=True)
class CreatePaymentIntentResponse:
    shoppingCart: Optional[ShoppingCartData] = None
    paymentIntentOutput: Optional[PaymentIntentOutput] = None
