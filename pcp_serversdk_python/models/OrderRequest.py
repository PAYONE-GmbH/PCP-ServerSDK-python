from dataclasses import dataclass
from typing import Optional

from .FundSplit import FundSplit
from .OrderItem import OrderItem
from .OrderType import OrderType
from .PaymentMethodSpecificInput import PaymentMethodSpecificInput
from .References import References


@dataclass(kw_only=True)
class OrderRequest:
    orderType: Optional[OrderType] = None
    orderReferences: Optional[References] = None
    items: Optional[list[OrderItem]] = None
    paymentMethodSpecificInput: Optional[PaymentMethodSpecificInput] = None
    fundSplit: Optional[FundSplit] = None
