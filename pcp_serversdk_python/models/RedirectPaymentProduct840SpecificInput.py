from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class RedirectPaymentProduct840SpecificInput:
    addressSelectionAtPayPal: Optional[bool] = False
