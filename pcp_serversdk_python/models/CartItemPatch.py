from typing import Optional
from dataclasses import dataclass
from .CartItemInvoiceData import CartItemInvoiceData
from .OrderLineDetailsPatch import OrderLineDetailsPatch


@dataclass(kw_only=True)
class CartItemPatch:
    invoiceData: Optional[CartItemInvoiceData] = None
    orderLineDetails: Optional[OrderLineDetailsPatch] = None
