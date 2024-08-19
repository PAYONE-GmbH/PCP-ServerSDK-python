from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class CheckoutReferences:
    merchantReference: Optional[str] = None
    merchantShopReference: Optional[str] = None
