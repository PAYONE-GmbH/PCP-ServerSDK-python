from typing import Optional, List
from dataclasses import dataclass
from .CartItemOrderStatus import CartItemOrderStatus
from .OrderLineDetailsInput import OrderLineDetailsInput

@dataclass(kw_only=True)
class OrderLineDetailsResult(OrderLineDetailsInput):
    id: Optional[str] = None
    status: Optional[List[CartItemOrderStatus]] = None
