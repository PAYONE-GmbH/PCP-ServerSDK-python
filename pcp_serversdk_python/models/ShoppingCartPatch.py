from typing import Optional, List
from dataclasses import dataclass
from .CartItemPatch import CartItemPatch


@dataclass(kw_only=True)
class ShoppingCartPatch:
    items: Optional[List[CartItemPatch]] = None
