from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class PaymentProduct840CustomerAccount:
    companyName: Optional[str] = None
    firstName: Optional[str] = None
    payerId: Optional[str] = None
    surname: Optional[str] = None
