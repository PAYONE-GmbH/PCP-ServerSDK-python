from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class CardFraudResults:
    avsResult: Optional[str] = None
