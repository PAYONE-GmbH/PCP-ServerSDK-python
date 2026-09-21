from dataclasses import dataclass
from typing import Optional

from .OrderItem import OrderItem
from .OrderType import OrderType
from .PaymentLinkSpecificInput import PaymentLinkSpecificInput
from .References import References


@dataclass(kw_only=True)
class CreatePayByLinkRequest:
    paymentLinkSpecificInput: PaymentLinkSpecificInput
    orderType: OrderType
    orderReferences: References
    items: Optional[list[OrderItem]] = None
