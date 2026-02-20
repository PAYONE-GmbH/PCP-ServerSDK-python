from dataclasses import dataclass
from typing import Optional

from .FundSplit import FundSplit
from .RefundPaymentResponse import RefundPaymentResponse
from .ShoppingCartResult import ShoppingCartResult


@dataclass(kw_only=True)
class ReturnResponse:
    returnPaymentResponse: Optional[RefundPaymentResponse] = None
    shoppingCart: Optional[ShoppingCartResult] = None
    fundSplit: Optional[FundSplit] = None
