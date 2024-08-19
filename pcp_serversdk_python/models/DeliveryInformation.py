from typing import Optional, List
from dataclasses import dataclass
from .CartItemInput import CartItemInput

@dataclass(kw_only=True)
class DeliveryInformation:
    items: Optional[List[CartItemInput]] = None
