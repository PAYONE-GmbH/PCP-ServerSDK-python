from dataclasses import dataclass
from typing import Optional

from .PayLinkStatusValue import PayLinkStatusValue
from .PaymentLinkOrder import PaymentLinkOrder


@dataclass(kw_only=True)
class CreatePayByLinkResponse:
    expirationDate: Optional[str] = None
    paymentLinkOrder: Optional[PaymentLinkOrder] = None
    status: Optional[PayLinkStatusValue] = None
    redirectionUrl: Optional[str] = None
    paymentLinkId: Optional[str] = None
