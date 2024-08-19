from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class CustomerDevice:
    ipAddress: Optional[str] = None
    deviceToken: Optional[str] = None
