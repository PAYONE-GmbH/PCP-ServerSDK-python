from dataclasses import dataclass
from typing import List, Optional

from .CartItemResult import CartItemResult


@dataclass(kw_only=True)
class ShoppingCartResult:
    items: Optional[List[CartItemResult]] = None
