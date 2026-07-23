from dataclasses import dataclass
from typing import Optional

from .CartItemInvoiceData import CartItemInvoiceData
from .OrderLineDetailsInput import OrderLineDetailsInput


@dataclass(kw_only=True)
class CartItemData:
    invoiceData: Optional[CartItemInvoiceData] = None
    orderLineDetails: Optional[OrderLineDetailsInput] = None
