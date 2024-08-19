from typing import Optional
from dataclasses import dataclass
from .CreatePaymentResponse import CreatePaymentResponse
from .ShoppingCartResult import ShoppingCartResult


@dataclass(kw_only=True)
class OrderResponse:
    createPaymentResponse: Optional[CreatePaymentResponse] = None
    shoppingCart: Optional[ShoppingCartResult] = None
