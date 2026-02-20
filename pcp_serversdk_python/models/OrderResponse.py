from dataclasses import dataclass
from typing import Optional

from .CreatePaymentResponse import CreatePaymentResponse
from .FundSplit import FundSplit
from .ShoppingCartResult import ShoppingCartResult


@dataclass(kw_only=True)
class OrderResponse:
    createPaymentResponse: Optional[CreatePaymentResponse] = None
    shoppingCart: Optional[ShoppingCartResult] = None
    fundSplit: Optional[FundSplit] = None
