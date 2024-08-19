from typing import Optional, List
from dataclasses import dataclass
from .CancelType import CancelType
from .CancellationReason import CancellationReason
from .CancelItem import CancelItem

@dataclass(kw_only=True)
class CancelRequest:
    cancelType: Optional[CancelType] = None
    cancellationReason: Optional[CancellationReason] = None
    cancelItems: Optional[List[CancelItem]] = None
