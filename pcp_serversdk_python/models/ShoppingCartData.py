from dataclasses import dataclass
from typing import Optional

from .CartItemData import CartItemData


@dataclass(kw_only=True)
class ShoppingCartData:
    items: Optional[list[CartItemData]] = None
