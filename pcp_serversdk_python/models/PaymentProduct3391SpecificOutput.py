from typing import Optional, List
from dataclasses import dataclass
from .InstallmentOption import InstallmentOption

@dataclass(kw_only=True)
class PaymentProduct3391SpecificOutput:
    installmentOptions: Optional[List[InstallmentOption]] = None
