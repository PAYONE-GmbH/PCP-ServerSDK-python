from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class PaymentCreationOutput:
    externalReference: Optional[str] = None
