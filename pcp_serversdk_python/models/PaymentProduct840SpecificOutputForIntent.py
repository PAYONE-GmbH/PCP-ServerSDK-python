from dataclasses import dataclass
from typing import Optional

from .Address import Address
from .PaymentProduct840CustomerAccountForIntent import (
    PaymentProduct840CustomerAccountForIntent,
)
from .ShippingAddress import ShippingAddress


@dataclass(kw_only=True)
class PaymentProduct840SpecificOutputForIntent:
    billingAddress: Optional[Address] = None
    customerAccount: Optional[PaymentProduct840CustomerAccountForIntent] = None
    payPalTransactionId: Optional[str] = None
    shippingAddress: Optional[ShippingAddress] = None
