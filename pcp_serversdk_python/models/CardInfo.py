from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class CardInfo:
    cardholderName: Optional[str] = None
