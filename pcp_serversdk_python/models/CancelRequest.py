from dataclasses import dataclass
from typing import Optional

from .CancelItem import CancelItem
from .CancellationReason import CancellationReason
from .CancelType import CancelType
from .FundSplit import FundSplit


@dataclass(kw_only=True)
class CancelRequest:
    cancelType: Optional[CancelType] = None
    cancellationReason: Optional[CancellationReason] = None
    cancelItems: Optional[list[CancelItem]] = None
    fundSplit: Optional[FundSplit] = None
