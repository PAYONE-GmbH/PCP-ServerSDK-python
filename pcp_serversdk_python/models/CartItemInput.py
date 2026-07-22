from dataclasses import dataclass
from typing import Optional

from .CartItemData import CartItemData
from .CartItemSupplierReferences import CartItemSupplierReferences


@dataclass(kw_only=True)
class CartItemInput(CartItemData):
    supplierReferences: Optional[CartItemSupplierReferences] = None
