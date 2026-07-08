from dataclasses import dataclass
from typing import Optional

from .CancellationReason import CancellationReason
from .FundSplit import FundSplit


@dataclass(kw_only=True)
class CancelPaymentRequest:
    cancellationReason: Optional[CancellationReason] = None
    amount: Optional[int] = None
    fundSplit: Optional[FundSplit] = None
