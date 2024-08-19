from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class CartItemInvoiceData:
    description: Optional[str] = None
