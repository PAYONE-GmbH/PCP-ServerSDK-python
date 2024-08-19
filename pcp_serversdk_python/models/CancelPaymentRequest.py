from typing import Optional
from dataclasses import dataclass
from .CancellationReason import CancellationReason

@dataclass(kw_only=True)
class CancelPaymentRequest:
    cancellationReason: Optional[CancellationReason] = None
