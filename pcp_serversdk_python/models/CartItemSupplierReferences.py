from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class CartItemSupplierReferences:
    """References of the seller of a cart item."""

    supplierId: Optional[str] = None
    """Identifier of the supplier/seller. Maximum length: 64 characters."""

    orderReference: Optional[str] = None
    """Order reference of the supplier/seller. Maximum length: 64 characters."""
