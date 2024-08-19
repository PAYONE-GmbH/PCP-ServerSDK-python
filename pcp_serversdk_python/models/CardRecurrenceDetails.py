from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class CardRecurrenceDetails:
    recurringPaymentSequenceIndicator: Optional[str] = None
