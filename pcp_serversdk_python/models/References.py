from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class References:
    descriptor: Optional[str] = None
    merchantReference: str
    merchantParameters: Optional[str] = None
