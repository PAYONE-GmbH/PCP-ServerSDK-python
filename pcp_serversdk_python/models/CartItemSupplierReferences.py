from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class CartItemSupplierReferences:
    """References of the seller of a cart item."""

    supplierId: str
    """Unique identifier for the supplier. Used for reporting to identify to which
    supplier the item belongs. Only allowed for marketplace merchants or if feature
    to ignore Marketplace fields is enabled in configuration.. Maximum length: 64
    characters."""

    orderReference: Optional[str] = None
    """Order reference of the supplier/seller. Maximum length: 64 characters."""
