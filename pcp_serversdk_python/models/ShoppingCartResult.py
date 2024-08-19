from typing import Optional, List
from dataclasses import dataclass
from .CartItemResult import CartItemResult


@dataclass(kw_only=True)
class ShoppingCartResult:
    items: Optional[List[CartItemResult]] = None
