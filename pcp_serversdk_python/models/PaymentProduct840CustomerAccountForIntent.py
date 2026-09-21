from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class PaymentProduct840CustomerAccountForIntent:
    companyName: Optional[str] = None
    firstName: Optional[str] = None
    surname: Optional[str] = None
    emailAddress: Optional[str] = None
