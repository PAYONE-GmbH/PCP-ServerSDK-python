from dataclasses import dataclass
from typing import Optional

from .CapturePaymentResponse import CapturePaymentResponse
from .FundSplit import FundSplit
from .ShoppingCartResult import ShoppingCartResult


@dataclass(kw_only=True)
class DeliverResponse:
    capturePaymentResponse: Optional[CapturePaymentResponse] = None
    shoppingCart: Optional[ShoppingCartResult] = None
    fundSplit: Optional[FundSplit] = None
