from dataclasses import dataclass
from typing import Optional

from .CartItemInvoiceData import CartItemInvoiceData
from .CartItemSupplierReferences import CartItemSupplierReferences
from .OrderLineDetailsPatch import OrderLineDetailsPatch


@dataclass(kw_only=True)
class CartItemPatch:
    invoiceData: Optional[CartItemInvoiceData] = None
    orderLineDetails: Optional[OrderLineDetailsPatch] = None
    supplierReferences: Optional[CartItemSupplierReferences] = None
