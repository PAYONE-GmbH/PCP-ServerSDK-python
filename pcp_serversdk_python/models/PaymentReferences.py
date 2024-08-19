from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class PaymentReferences:
    merchantReference: Optional[str] = None
