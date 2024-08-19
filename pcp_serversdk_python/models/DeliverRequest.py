from typing import Optional, List
from dataclasses import dataclass
from .CancellationReason import CancellationReason
from .DeliverItem import DeliverItem
from .DeliverType import DeliverType

@dataclass(kw_only=True)
class DeliverRequest:
    deliverType: Optional[DeliverType] = None
    isFinal: bool = False
    cancellationReason: Optional[CancellationReason] = None
    deliverItems: Optional[List[DeliverItem]] = None
