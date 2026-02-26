from dataclasses import dataclass
from typing import Optional

from .CartItemInvoiceData import CartItemInvoiceData
from .CartItemSupplierReferences import CartItemSupplierReferences
from .OrderLineDetailsResult import OrderLineDetailsResult


@dataclass(kw_only=True)
class CartItemResult:
    invoiceData: Optional[CartItemInvoiceData] = None
    orderLineDetails: Optional[OrderLineDetailsResult] = None
    supplierReferences: Optional[CartItemSupplierReferences] = None
