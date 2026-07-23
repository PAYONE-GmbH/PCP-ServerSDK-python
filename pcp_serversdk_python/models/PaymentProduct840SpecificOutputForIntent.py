from dataclasses import dataclass
from typing import Optional

from .PaymentProduct840SpecificOutputData import PaymentProduct840SpecificOutputData
from .ShippingAddress import ShippingAddress


@dataclass(kw_only=True)
class PaymentProduct840SpecificOutputForIntent(PaymentProduct840SpecificOutputData):
    shippingAddress: Optional[ShippingAddress] = None
