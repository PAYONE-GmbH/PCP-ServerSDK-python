from dataclasses import dataclass
from typing import Optional

from .FundSplit import FundSplit
from .ReturnItem import ReturnItem
from .ReturnType import ReturnType


@dataclass(kw_only=True)
class ReturnRequest:
    returnType: Optional[ReturnType] = None
    returnReason: Optional[str] = None
    returnItems: Optional[list[ReturnItem]] = None
    fundSplit: Optional[FundSplit] = None
