from dataclasses import dataclass
from typing import Optional

from .Address import Address
from .PaymentProduct840SpecificOutputData import PaymentProduct840SpecificOutputData


@dataclass(kw_only=True)
class PaymentProduct840SpecificOutput(PaymentProduct840SpecificOutputData):
    shippingAddress: Optional[Address] = None
