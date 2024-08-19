from typing import Optional
from dataclasses import dataclass
from .CapturePaymentResponse import CapturePaymentResponse
from .ShoppingCartResult import ShoppingCartResult


@dataclass(kw_only=True)
class DeliverResponse:
    capturePaymentResponse: Optional[CapturePaymentResponse] = None
    shoppingCart: Optional[ShoppingCartResult] = None
