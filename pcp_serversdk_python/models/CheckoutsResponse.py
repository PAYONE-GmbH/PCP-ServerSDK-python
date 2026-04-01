from dataclasses import dataclass
from typing import Optional

from .CheckoutResponse import CheckoutResponse


@dataclass(kw_only=True)
class CheckoutsResponse:
    numberOfCheckouts: Optional[int] = None
    checkouts: Optional[list[CheckoutResponse]] = None
