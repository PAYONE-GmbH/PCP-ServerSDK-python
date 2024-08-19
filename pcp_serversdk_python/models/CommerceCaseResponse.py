from typing import Optional, List
from dataclasses import dataclass
from .CheckoutResponse import CheckoutResponse
from .CreationDateTime import CreationDateTime
from .Customer import Customer


@dataclass(kw_only=True)
class CommerceCaseResponse:
    merchantReference: Optional[str] = None
    commerceCaseId: Optional[str] = None
    customer: Optional[Customer] = None
    checkouts: Optional[List[CheckoutResponse]] = None
    creationDateTime: Optional[CreationDateTime] = None
